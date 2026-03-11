##GPG commands

#### Basic commands to get you started with gpg
 
* List keys

```bash
gpg --list-keys
gpg --list
gpg --list-secret-keys
gpg --list-public-keys
gpg --list-key
```

**Import**

```bash
gpg --import *
gpg --list-keys
gpg --edit-key BBBF86A5
gpg --list-keys
gpg --list-key
```

**Config**

```bash
gpg --list-config
gpg --list-public-keys
gpg --list-secret-keys
vim gpg.conf
```

**Secrets**

```bash
gpg --list-sig
gpg --list-secret-keys
gpg --list-trustdb
```

**Sign and upload**

```bash
gpg --refresh-keys
gpg --list-key
gpg --sign-key F5DB08D4
```

**Upload**

```bash
gpg --list-sigs
gpg --send-keys
```

**Grep all your keys**

```bash
gpg --list-keys | grep ^pub | awk '{ print $2 }' | cut -d/ -f 2
```

**Decrypt a file using your key**

```bash
gpg --decrypt secret.gpg
```

**Import a persons key**

```bash
gpg --import personx-2345678c.txt
```

 
