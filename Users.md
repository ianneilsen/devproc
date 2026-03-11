## Users on nix

#### Good Reads

https://unix.stackexchange.com/questions/1373/how-do-i-switch-from-an-unknown-shell-to-bash


#### su to user with nologin

```bash
	su - named -s /bin/bash


export UGIDLIMIT=1000
awk -v LIMIT=$UGIDLIMIT -F: '($3>=LIMIT) && ($3!=65534)' /etc/passwd > /root/tmp/clone/pass.mig
awk -v LIMIT=$UGIDLIMIT -F: '($3>=LIMIT) && ($3!=65534)' /etc/group > /root/tmp/clone/group.mig
awk -v LIMIT=$UGIDLIMIT -F: '($3>=LIMIT) && ($3!=65534) {print $1}' /etc/passwd | tee - |egrep -f - /etc/shadow  > /root/tmp/clone/shadow.mig
cp /etc/gshadow /root/tmp/clone/gshadow.mig
tar -zcvpf /root/tmp/clone/mail.tar.gz /var/spool/mail
tar -zcvpf /root/tmp/clone/home.tar.gz /home
tar -zcvpf /root/tmp/clone/openvpn.tar.gz /etc/openvpn
tar -zcvpf /root/tmp/clone.tar.gz /root/tmp/clone

```