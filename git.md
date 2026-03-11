## git


#### Good reads

https://nvie.com/posts/a-successful-git-branching-model/?

https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html


#### Great page of useful git commands

https://orga.cat/posts/most-useful-git-commands



Clean git commit history

```bash
# Install it
 install git-filter-repo

# Remove specific files from all history
git filter-repo --invert-paths --path path/to/sensitive-file

# Or replace specific strings (passwords, domains) with ***REMOVED***
git filter-repo --replace-text expressions.txt
```

Where `expressions.txt` contains lines like:

```bash
myOldPassword==>***REMOVED***
secret.domain.com==>example.com
```

#### steps using filter-repo
```bash
git remote remove origin

# Run the filter
git filter-repo --replace-text expressions.txt

# Re-add the remote and force push
git remote add origin git@github.com:youruser/yourrepo.git
git push --force --all
git push --force --tags
```

### Grepping git history manually

```bash
# Search every blob in every commit for a specific string
git log --all -p -S "your-old-password" --color

# Or use grep across all history (slower but supports regex)
git rev-list --all | xargs git grep -l "old\.domain\.com"

# Check a specific pattern like IPs
git rev-list --all | xargs git grep -lE "\b203\.0\.113\.\d{1,3}\b"

# Nuclear option — dump every blob and grep the lot
git rev-list --all | while read sha; do
    git diff-tree --no-commit-id -r "$sha" 2>/dev/null | awk '{print $4}' | while read blob; do
        git cat-file -p "$blob" 2>/dev/null
    done
done | grep -n "sensitive-string"
```