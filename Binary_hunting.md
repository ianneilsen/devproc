# Binary Hunting

Source: [TrustedSec - Malware on Linux](https://www.trustedsec.com/2018/04/malware-linux/)

## Finding Binaries That Don’t Belong

```bash
find /proc/*/exe -exec readlink {} + | xargs rpm -qf | grep “not owned”
find /proc/*/exe -exec readlink {} + | xargs dpkg -S | grep “no path”
```


## Verifying Running Binaries Match Package Contents

```bash
find /proc/*/exe -exec readlink {} + | xargs rpm -qf | xargs rpm -V
find /proc/*/exe -exec readlink {} + | xargs dpkg -S | cut -d: -f1 | xargs dpkg -V
```


## Verify All

```bash
rpm -Va
dpkg -V
```


## Reading the Results

The output should show any binaries that belong to packages, calculate the hash of the binary, and compare it to the one saved when the package was installed or updated. The below output is for Redhat based systems. Debian based systems with dpkg don’t verify a lot of these, so only “5” is shown if the binary was modified.

| Flag | Meaning |
|------|---------|
| `S`  | File size differs |
| `M`  | Mode differs (includes permissions and file type) |
| `5`  | Digest (formerly MD5 sum) differs |
| `D`  | Device major/minor number mismatch |
| `L`  | readLink(2) path mismatch |
| `U`  | User ownership differs |
| `G`  | Group ownership differs |
| `T`  | mTime differs |
| `P`  | Capabilities differ |

## Check for RAW Sockets

Something we’ve been seeing more often is RAW socket backdoors. These listen for an incoming packet and trigger an event. One example is that the recent write-up on the “Chaos” backdoor links to the write-ups will be below, along with an example that popped up while searching for a raw socket backdoor on github. For this check we are just going to see what processes are using RAW sockets. There are not a lot of common programs using them, so this could narrow down what processes to look at if you think you were compromised.

### Check for Binaries with Raw Sockets Listening

```bash
netstat -lwp
ss -lwp
lsof | grep RAW
```

## Checking for Possible Injected Memory

This one on its own will have all sorts of false positives. RWX memory (Read Write and Execute) is used by a lot of programs, most of which are interpreted languages, so things like python and java, or things using any libraries that parse scripts, will have this and it will be normal. If you find a lot of entries of RWX memory and that process isn’t python or java, you should probably look a little closer at it. This command will list the process ids with RWX memory. Things like gnome will be normal as well, but things like cron or any other normal process shouldn’t have any.

### Command to Find PIDs

```bash
grep -r “rwx” /proc/*/maps | cut -d/ -f 3 | uniq -c | sort -nr
```

## Check for Modified PAM Modules

One common backdoor is inserting or replacing a PAM module for authentication. This can allow for remote access and also allow for an attacker to su to root from any user. This backdoor also doesn’t care about changes to /etc/passwd so all the original passwords and changed ones will still work; however, it has the actual password the attacker will use embedded into it. This is, in my opinion, a really dangerous type of backdoor due to the type of access it gives. You can use normal protocols with legitimate login entries, so there is obviously no malicious network activity.

### Verify PAM Modules

```bash
find /lib64/security/ | xargs rpm -qf | grep “not owned”
find /lib64/security/ | xargs rpm -qf | grep -v “not “ | xargs rpm -V
```


## Last but Not Least — SSH Access

An extremely simple way to keep access that doesn’t require dropping a binary is simply adding a ssh key into the authorized_keys file for a specific user and allow the attacker to ssh in like a normal user. This is also one of the hardest methods to detect because you need to figure out if the ssh keys are legit or malicious, which requires users to verify that only their keys are in that file. An attacker could also just steal the key of a user if they were compromised before.

### List .ssh Folder for All Users

```bash
cat /etc/passwd | cut -d: -f 6 | xargs -I@ /bin/sh -c “echo @; ls -al @/.ssh/ 2>/dev/null”
```
