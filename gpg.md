##GPG commands

#### Basic commands to get you started with gpg
 
* List keys
 
    gpg --list-keys
    gpg --list
    gpg --list-secret-keys 
    gpg --list-public-keys 
    gpg --list-key

**Import**

    gpg --import *
    gpg --list-keys
    gpg --edit-key BBBF86A5
    gpg --list-keys
    gpg --list-key

**Config**

    gpg --list-config 
    gpg --list-public-keys 
    gpg --list-secret-keys 
    vim gpg.conf 

**Secrets**

    gpg --list-sig
    gpg --list-secret-keys 
    gpg --list-trustdb 

**Sign and upload**

    gpg --refresh-keys 
    gpg --list-key
    gpg --sign-key F5DB08D4
 
**Upload**

    gpg --list-sigs 
    gpg --send-keys 
    gpg --send-keys 

**Grep all your keys**

    gpg --list-keys | grep ^pub | awk '{ print $2 }' | cut -d/ -f 2

**Decrypt a file using your key**

`gpg --decrypt secret.gpg` 

**Import a persons key**

`gpg --import personx-2345678c.txt` 

 
