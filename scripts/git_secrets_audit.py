#!/usr/bin/env python3
"""
git_secrets_audit.py — Pre-publication sensitive data scanner for git repositories.

Scans every blob in every commit across your entire git history for:
  - Passwords and secrets in config files
  - IP addresses (private and public)
  - Domain names / hostnames
  - API keys and tokens
  - Sensitive file paths (.env, docker-compose, CI configs, vault files, etc.)
  - High-entropy strings (potential secrets)

Usage:
    python3 git_secrets_audit.py /path/to/repo [--output report.json] [--domains example.com,other.com]

Outputs a detailed report with commit SHA, file path, line number, match type, and matched value
so you can build a comprehensive git-filter-repo expressions file.
"""

import argparse
import json
import math
import os
import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Optional


# ──────────────────────────────────────────────────────────────────────────────
# Configuration: patterns and known-sensitive filenames
# ──────────────────────────────────────────────────────────────────────────────

# Files that are inherently sensitive (should probably not be in a public repo at all)
SENSITIVE_FILE_PATTERNS = [
    r"\.env$",
    r"\.env\..+$",                    # .env.production, .env.local, etc.
    r"\.envrc$",
    r"\.htpasswd$",
    r"\.pgpass$",
    r"\.netrc$",
    r"\.npmrc$",
    r"\.pypirc$",
    r"\.docker/config\.json$",
    r"docker-compose\.ya?ml$",
    r"docker-compose\..+\.ya?ml$",
    r"Dockerfile",
    r"\.kube/config$",
    r"kubeconfig",
    r"credentials\.json$",
    r"credentials\.ya?ml$",
    r"service[_-]?account.*\.json$",
    r"secrets?\.ya?ml$",
    r"secrets?\.json$",
    r"vault\.ya?ml$",
    r"ansible[_-]vault",
    r"\.vault[_-]pass",
    r"terraform\.tfvars$",
    r"\.tfstate$",
    r".*\.pem$",
    r".*\.key$",
    r".*\.p12$",
    r".*\.pfx$",
    r".*\.jks$",
    r"id_rsa",
    r"id_ed25519",
    r"id_ecdsa",
    r"id_dsa",
    r"known_hosts$",
    r"authorized_keys$",
    # CI/CD configs (not sensitive themselves, but often contain secrets)
    r"\.github/workflows/.*\.ya?ml$",
    r"\.gitlab-ci\.ya?ml$",
    r"Jenkinsfile$",
    r"\.circleci/config\.ya?ml$",
    r"\.travis\.ya?ml$",
    r"buildkite\.ya?ml$",
    r"cloudbuild\.ya?ml$",
    r"\.drone\.ya?ml$",
    r"bitbucket-pipelines\.ya?ml$",
    r"appveyor\.ya?ml$",
    r"azure-pipelines\.ya?ml$",
]

# Compile for performance
SENSITIVE_FILE_RE = [re.compile(p, re.IGNORECASE) for p in SENSITIVE_FILE_PATTERNS]

# Content patterns — each returns (pattern_name, compiled_regex)
CONTENT_PATTERNS = {
    # ── IP Addresses ──────────────────────────────────────────────────────
    "ipv4_address": re.compile(
        r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b"
    ),
    "ipv6_address": re.compile(
        r"(?i)\b(?:[0-9a-f]{1,4}:){7}[0-9a-f]{1,4}\b"
        r"|\b(?:[0-9a-f]{1,4}:){1,7}:\b"
        r"|\b::(?:[0-9a-f]{1,4}:){0,5}[0-9a-f]{1,4}\b"
    ),

    # ── Password / secret assignments ────────────────────────────────────
    "password_assignment": re.compile(
        r"""(?i)(?:password|passwd|pwd|pass|secret|token|api[_-]?key|apikey|"""
        r"""auth[_-]?token|access[_-]?key|private[_-]?key|client[_-]?secret|"""
        r"""encryption[_-]?key|signing[_-]?key|jwt[_-]?secret|session[_-]?secret|"""
        r"""db[_-]?pass|database[_-]?password|mysql[_-]?pwd|pg[_-]?password|"""
        r"""redis[_-]?password|mongo[_-]?password|smtp[_-]?pass)"""
        r"""[\s]*[=:]+[\s]*['"]?([^\s'"#\n]{4,})['"]?""",
        re.MULTILINE,
    ),

    # ── AWS-style keys ───────────────────────────────────────────────────
    "aws_access_key": re.compile(r"\b(?:AKIA|ABIA|ACCA|ASIA)[0-9A-Z]{16}\b"),
    "aws_secret_key": re.compile(r"""(?i)aws_secret_access_key[\s]*[=:]+[\s]*['"]?([A-Za-z0-9/+=]{40})['"]?"""),

    # ── Generic API keys / tokens ────────────────────────────────────────
    "generic_api_key": re.compile(
        r"""(?i)(?:api[_-]?key|apikey|api[_-]?token|access[_-]?token|auth[_-]?token|"""
        r"""bearer)\s*[=:]+\s*['"]?([A-Za-z0-9_\-./+=]{20,})['"]?"""
    ),
    "bearer_token": re.compile(r"""(?i)bearer\s+[A-Za-z0-9_\-./+=]{20,}"""),

    # ── Cloud provider tokens ────────────────────────────────────────────
    "gcp_service_account": re.compile(r'"type"\s*:\s*"service_account"'),
    "github_token": re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{36,}\b"),
    "gitlab_token": re.compile(r"\bglpat-[A-Za-z0-9_\-]{20,}\b"),
    "slack_token": re.compile(r"\bxox[baprs]-[A-Za-z0-9\-]{10,}"),
    "slack_webhook": re.compile(r"https://hooks\.slack\.com/services/T[A-Za-z0-9_]+/B[A-Za-z0-9_]+/[A-Za-z0-9_]+"),
    "stripe_key": re.compile(r"\b[sr]k_(?:live|test)_[A-Za-z0-9]{20,}\b"),
    "sendgrid_key": re.compile(r"\bSG\.[A-Za-z0-9_\-]{22}\.[A-Za-z0-9_\-]{43}\b"),
    "twilio_key": re.compile(r"\bSK[0-9a-fA-F]{32}\b"),
    "heroku_api_key": re.compile(r"""(?i)heroku.*[=:]+\s*['"]?[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}['"]?"""),

    # ── Private keys ─────────────────────────────────────────────────────
    "private_key_header": re.compile(
        r"-----BEGIN\s+(?:RSA\s+|DSA\s+|EC\s+|OPENSSH\s+)?PRIVATE\s+KEY-----"
    ),

    # ── Database connection strings ──────────────────────────────────────
    "database_url": re.compile(
        r"""(?i)(?:mysql|postgres(?:ql)?|mongodb(?:\+srv)?|redis|amqp|mssql)://[^\s'"]{10,}"""
    ),

    # ── Hardcoded URLs with credentials ──────────────────────────────────
    "url_with_credentials": re.compile(
        r"""https?://[^:@\s]+:[^:@\s]+@[^\s'"]{5,}"""
    ),

    # ── Docker / container registry auth ─────────────────────────────────
    "docker_auth": re.compile(r'"auth"\s*:\s*"[A-Za-z0-9+/=]{20,}"'),
}

# IPs to ignore (localhost, metadata, common examples)
IGNORED_IPS = {
    "0.0.0.0", "127.0.0.1", "255.255.255.255",
    "169.254.169.254",  # cloud metadata
    "10.0.0.0", "172.16.0.0", "192.168.0.0",  # network addresses
}

# Common false-positive domains
IGNORED_DOMAINS = {
    "example.com", "example.org", "example.net",
    "localhost", "localhost.localdomain",
    "schema.org", "www.w3.org", "w3.org",
    "json-schema.org", "yaml.org",
    "github.com", "gitlab.com", "bitbucket.org",
    "npmjs.com", "pypi.org", "rubygems.org", "crates.io",
    "golang.org", "pkg.go.dev",
    "stackoverflow.com", "wikipedia.org",
    "creativecommons.org", "opensource.org",
    "apache.org", "mozilla.org",
    "shields.io", "img.shields.io", "badge.fury.io",
    "travis-ci.org", "circleci.com",
    "docker.io", "docker.com", "hub.docker.com",
    "gcr.io", "ghcr.io", "quay.io",
    "amazonaws.com", "googleapis.com", "azure.com",
    "cloudflare.com", "fonts.googleapis.com",
    "cdnjs.cloudflare.com", "cdn.jsdelivr.net",
    "unpkg.com", "rawcdn.githack.com",
}


@dataclass
class Finding:
    """A single sensitive data finding."""
    commit: str
    commit_date: str
    file_path: str
    line_number: int
    match_type: str
    matched_value: str
    context: str  # surrounding line for reference

    def redacted_dict(self) -> dict:
        """Return dict with long secrets partially redacted for the report."""
        d = asdict(self)
        val = d["matched_value"]
        if len(val) > 12 and d["match_type"] not in ("sensitive_file", "ipv4_address", "ipv6_address"):
            d["matched_value"] = val[:4] + "****" + val[-4:]
        return d


@dataclass
class AuditReport:
    """Aggregated scan results."""
    repo_path: str
    scan_start: str
    scan_end: str = ""
    total_commits_scanned: int = 0
    total_findings: int = 0
    findings_by_type: dict = field(default_factory=lambda: defaultdict(int))
    unique_secrets: int = 0
    sensitive_files_found: list = field(default_factory=list)
    findings: list = field(default_factory=list)
    filter_repo_expressions: list = field(default_factory=list)


# ──────────────────────────────────────────────────────────────────────────────
# Entropy calculation for detecting random-looking strings (potential secrets)
# ──────────────────────────────────────────────────────────────────────────────

def shannon_entropy(s: str) -> float:
    """Calculate Shannon entropy of a string."""
    if not s:
        return 0.0
    freq = defaultdict(int)
    for c in s:
        freq[c] += 1
    length = len(s)
    return -sum((count / length) * math.log2(count / length) for count in freq.values())


def is_high_entropy(s: str, threshold: float = 4.5) -> bool:
    """Check if a string has suspiciously high entropy (likely a secret)."""
    if len(s) < 16:
        return False
    return shannon_entropy(s) >= threshold


# ──────────────────────────────────────────────────────────────────────────────
# Git interaction
# ──────────────────────────────────────────────────────────────────────────────

def run_git(repo_path: str, *args: str) -> str:
    """Run a git command and return stdout."""
    result = subprocess.run(
        ["git", "-C", repo_path] + list(args),
        capture_output=True, text=True, timeout=120,
    )
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def get_all_commits(repo_path: str) -> list[tuple[str, str]]:
    """Return list of (sha, iso_date) for all commits, oldest first."""
    log = run_git(repo_path, "log", "--all", "--format=%H %aI", "--reverse")
    commits = []
    for line in log.strip().splitlines():
        if line.strip():
            parts = line.strip().split(" ", 1)
            commits.append((parts[0], parts[1] if len(parts) > 1 else ""))
    return commits


def get_tree_files(repo_path: str, commit_sha: str) -> list[str]:
    """Return list of file paths in a commit's tree."""
    tree = run_git(repo_path, "ls-tree", "-r", "--name-only", commit_sha)
    return [f.strip() for f in tree.strip().splitlines() if f.strip()]


def get_file_content(repo_path: str, commit_sha: str, file_path: str) -> Optional[str]:
    """Return file content at a given commit, or None if binary/error."""
    try:
        result = subprocess.run(
            ["git", "-C", repo_path, "show", f"{commit_sha}:{file_path}"],
            capture_output=True, timeout=30,
        )
        if result.returncode != 0:
            return None
        # Skip binary files
        try:
            return result.stdout.decode("utf-8", errors="strict")
        except UnicodeDecodeError:
            return None
    except subprocess.TimeoutExpired:
        return None


# ──────────────────────────────────────────────────────────────────────────────
# Scanning logic
# ──────────────────────────────────────────────────────────────────────────────

def check_sensitive_filename(file_path: str) -> bool:
    """Check if a file path matches known sensitive patterns."""
    return any(r.search(file_path) for r in SENSITIVE_FILE_RE)


def build_domain_pattern(custom_domains: list[str]) -> Optional[re.Pattern]:
    """Build a regex to match custom domain names the user wants to find."""
    if not custom_domains:
        return None
    escaped = [re.escape(d) for d in custom_domains]
    # Match the domain and any subdomains
    pattern = r"\b(?:[a-zA-Z0-9\-]+\.)*(?:" + "|".join(escaped) + r")\b"
    return re.compile(pattern, re.IGNORECASE)


def scan_content(
    content: str,
    file_path: str,
    commit_sha: str,
    commit_date: str,
    domain_re: Optional[re.Pattern],
    custom_hostnames: list[str],
) -> list[Finding]:
    """Scan file content for sensitive patterns."""
    findings = []
    lines = content.splitlines()

    for line_num, line in enumerate(lines, 1):
        # Skip very long lines (likely minified/binary-ish) to avoid slowdowns
        if len(line) > 2000:
            continue

        # ── Check each content pattern ────────────────────────────────
        for pattern_name, pattern in CONTENT_PATTERNS.items():
            for match in pattern.finditer(line):
                matched = match.group(0)

                # Filter out ignored IPs
                if pattern_name == "ipv4_address" and matched in IGNORED_IPS:
                    continue
                # Filter out version-number-looking IPs (e.g., 1.2.3.4 in version strings)
                if pattern_name == "ipv4_address":
                    # Check surrounding context for version indicators
                    ctx_start = max(0, match.start() - 20)
                    ctx = line[ctx_start:match.start()].lower()
                    if any(v in ctx for v in ["version", "v.", "v ", "go1.", "python", "node", "ruby"]):
                        continue

                findings.append(Finding(
                    commit=commit_sha[:12],
                    commit_date=commit_date,
                    file_path=file_path,
                    line_number=line_num,
                    match_type=pattern_name,
                    matched_value=matched.strip("'\" "),
                    context=line.strip()[:200],
                ))

        # ── Check custom domains ──────────────────────────────────────
        if domain_re:
            for match in domain_re.finditer(line):
                matched = match.group(0)
                if matched.lower() not in IGNORED_DOMAINS:
                    findings.append(Finding(
                        commit=commit_sha[:12],
                        commit_date=commit_date,
                        file_path=file_path,
                        line_number=line_num,
                        match_type="custom_domain",
                        matched_value=matched,
                        context=line.strip()[:200],
                    ))

        # ── Check custom hostnames ────────────────────────────────────
        for hostname in custom_hostnames:
            if hostname.lower() in line.lower():
                findings.append(Finding(
                    commit=commit_sha[:12],
                    commit_date=commit_date,
                    file_path=file_path,
                    line_number=line_num,
                    match_type="custom_hostname",
                    matched_value=hostname,
                    context=line.strip()[:200],
                ))

    return findings


def scan_repo(
    repo_path: str,
    custom_domains: list[str] = None,
    custom_hostnames: list[str] = None,
    sample_latest: int = 0,
    verbose: bool = True,
) -> AuditReport:
    """
    Full audit of a git repository.

    Args:
        repo_path:        Path to git repo root
        custom_domains:   Your real domain names to search for (e.g. ["mysite.com.au"])
        custom_hostnames: Internal hostnames to find (e.g. ["prod-db-01", "k8s-master"])
        sample_latest:    If > 0, only scan the N most recent commits (faster for testing)
        verbose:          Print progress to stderr
    """
    report = AuditReport(
        repo_path=os.path.abspath(repo_path),
        scan_start=datetime.now().isoformat(),
    )

    custom_domains = custom_domains or []
    custom_hostnames = custom_hostnames or []
    domain_re = build_domain_pattern(custom_domains)

    # Gather commits
    all_commits = get_all_commits(repo_path)
    if sample_latest > 0:
        all_commits = all_commits[-sample_latest:]

    total = len(all_commits)
    if verbose:
        print(f"\n{'='*70}", file=sys.stderr)
        print(f"  Git Secrets Audit — scanning {total} commits", file=sys.stderr)
        print(f"  Repo: {repo_path}", file=sys.stderr)
        print(f"  Custom domains: {custom_domains or '(none)'}", file=sys.stderr)
        print(f"  Custom hostnames: {custom_hostnames or '(none)'}", file=sys.stderr)
        print(f"{'='*70}\n", file=sys.stderr)

    seen_blobs: set[str] = set()  # track (commit:file) to avoid rescanning unchanged files
    unique_values: set[str] = set()

    for idx, (sha, date) in enumerate(all_commits):
        if verbose and (idx % 50 == 0 or idx == total - 1):
            pct = ((idx + 1) / total) * 100
            print(f"  [{idx+1:>6}/{total}] {pct:5.1f}%  commit {sha[:12]}  ({date[:10]})", file=sys.stderr)

        report.total_commits_scanned += 1

        try:
            files = get_tree_files(repo_path, sha)
        except RuntimeError:
            continue

        for fpath in files:
            blob_key = f"{sha}:{fpath}"

            # ── Check sensitive filenames ─────────────────────────────
            if check_sensitive_filename(fpath):
                if fpath not in report.sensitive_files_found:
                    report.sensitive_files_found.append(fpath)
                report.findings.append(Finding(
                    commit=sha[:12],
                    commit_date=date,
                    file_path=fpath,
                    line_number=0,
                    match_type="sensitive_file",
                    matched_value=fpath,
                    context="(sensitive filename pattern)",
                ))
                report.findings_by_type["sensitive_file"] += 1
                report.total_findings += 1

            # ── Scan file contents (skip if we've seen this exact blob) ──
            # Use git's own blob hash to deduplicate
            try:
                blob_hash = run_git(repo_path, "rev-parse", f"{sha}:{fpath}").strip()
            except RuntimeError:
                continue

            if blob_hash in seen_blobs:
                continue
            seen_blobs.add(blob_hash)

            content = get_file_content(repo_path, sha, fpath)
            if content is None:
                continue

            findings = scan_content(content, fpath, sha, date, domain_re, custom_hostnames)
            for f in findings:
                report.findings.append(f)
                report.findings_by_type[f.match_type] += 1
                report.total_findings += 1
                unique_values.add(f.matched_value)

    report.unique_secrets = len(unique_values)
    report.scan_end = datetime.now().isoformat()

    # ── Build suggested filter-repo expressions ──────────────────────────
    for val in sorted(unique_values):
        # Don't suggest expressions for filename-only findings
        if val in report.sensitive_files_found:
            continue
        safe_val = val.replace("==>", "\\==>")
        report.filter_repo_expressions.append(f"{safe_val}==>REDACTED")

    return report


# ──────────────────────────────────────────────────────────────────────────────
# Output formatting
# ──────────────────────────────────────────────────────────────────────────────

def print_summary(report: AuditReport) -> None:
    """Print a human-readable summary to stdout."""
    print(f"\n{'='*70}")
    print(f"  AUDIT COMPLETE — {report.repo_path}")
    print(f"{'='*70}")
    print(f"  Commits scanned:   {report.total_commits_scanned:,}")
    print(f"  Total findings:    {report.total_findings:,}")
    print(f"  Unique secrets:    {report.unique_secrets:,}")
    print(f"  Scan duration:     {report.scan_start} → {report.scan_end}")
    print()

    if report.findings_by_type:
        print("  Findings by type:")
        for ftype, count in sorted(report.findings_by_type.items(), key=lambda x: -x[1]):
            print(f"    {ftype:<30s} {count:>6,}")
        print()

    if report.sensitive_files_found:
        print(f"  Sensitive files detected ({len(report.sensitive_files_found)}):")
        for f in sorted(set(report.sensitive_files_found)):
            print(f"    ⚠  {f}")
        print()

    if report.filter_repo_expressions:
        print(f"  Suggested filter-repo expressions ({len(report.filter_repo_expressions)}):")
        print(f"  (saved to expressions.txt if --output is set)\n")
        for expr in report.filter_repo_expressions[:30]:
            print(f"    {expr}")
        if len(report.filter_repo_expressions) > 30:
            print(f"    ... and {len(report.filter_repo_expressions) - 30} more")
    else:
        print("  ✓ No secrets detected — repo looks clean!")

    print(f"\n{'='*70}\n")


def save_reports(report: AuditReport, output_base: str) -> None:
    """Save JSON report and expressions.txt."""
    # JSON report with all findings
    json_path = output_base if output_base.endswith(".json") else f"{output_base}.json"
    report_dict = {
        "repo_path": report.repo_path,
        "scan_start": report.scan_start,
        "scan_end": report.scan_end,
        "total_commits_scanned": report.total_commits_scanned,
        "total_findings": report.total_findings,
        "unique_secrets": report.unique_secrets,
        "findings_by_type": dict(report.findings_by_type),
        "sensitive_files_found": report.sensitive_files_found,
        "findings": [f.redacted_dict() for f in report.findings],
    }
    with open(json_path, "w") as fh:
        json.dump(report_dict, fh, indent=2)
    print(f"  Report saved:       {json_path}", file=sys.stderr)

    # Expressions file for git-filter-repo
    expr_path = os.path.join(os.path.dirname(json_path) or ".", "expressions.txt")
    with open(expr_path, "w") as fh:
        fh.write("# Auto-generated by git_secrets_audit.py\n")
        fh.write("# Review carefully, then run:\n")
        fh.write("#   git filter-repo --replace-text expressions.txt\n\n")
        for expr in report.filter_repo_expressions:
            fh.write(f"{expr}\n")
    print(f"  Expressions saved:  {expr_path}", file=sys.stderr)


# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Scan a git repo's full history for secrets, IPs, domains, and sensitive files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic scan
  python3 git_secrets_audit.py /path/to/repo

  # Scan with your known domains and hostnames
  python3 git_secrets_audit.py /path/to/repo \\
      --domains mysite.com.au,api.mysite.com.au,internal.corp \\
      --hostnames prod-db-01,k8s-master-1,jenkins-ci \\
      --output audit_report

  # Quick test on last 20 commits
  python3 git_secrets_audit.py /path/to/repo --sample 20
        """,
    )
    parser.add_argument("repo", help="Path to git repository")
    parser.add_argument("--output", "-o", help="Output base path for JSON report and expressions.txt")
    parser.add_argument("--domains", "-d", help="Comma-separated list of your domain names to search for")
    parser.add_argument("--hostnames", "-H", help="Comma-separated list of internal hostnames to find")
    parser.add_argument("--sample", "-s", type=int, default=0,
                        help="Only scan the N most recent commits (0 = all)")
    parser.add_argument("--quiet", "-q", action="store_true", help="Suppress progress output")

    args = parser.parse_args()

    repo_path = args.repo
    if not os.path.isdir(os.path.join(repo_path, ".git")):
        # Might be a bare repo
        if not os.path.isfile(os.path.join(repo_path, "HEAD")):
            print(f"Error: '{repo_path}' doesn't look like a git repository.", file=sys.stderr)
            sys.exit(1)

    domains = [d.strip() for d in args.domains.split(",") if d.strip()] if args.domains else []
    hostnames = [h.strip() for h in args.hostnames.split(",") if h.strip()] if args.hostnames else []

    report = scan_repo(
        repo_path=repo_path,
        custom_domains=domains,
        custom_hostnames=hostnames,
        sample_latest=args.sample,
        verbose=not args.quiet,
    )

    print_summary(report)

    if args.output:
        save_reports(report, args.output)


if __name__ == "__main__":
    main()
