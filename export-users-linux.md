export UGIDLIMIT=1000

awk -v LIMIT=$UGIDLIMIT -F: '($3>=LIMIT) && ($3!=65534)' /etc/passwd > /root/tmp/central-eu-clone/pass.mig

awk -v LIMIT=$UGIDLIMIT -F: '($3>=LIMIT) && ($3!=65534)' /etc/group > /root/tmp/central-eu-clone/group.mig

awk -v LIMIT=$UGIDLIMIT -F: '($3>=LIMIT) && ($3!=65534) {print $1}' /etc/passwd | tee - |egrep -f - /etc/shadow  > /root/tmp/central-eu-clone/shadow.mig

cp /etc/gshadow /root/tmp/central-eu-clone/gshadow.mig

tar -zcvpf /root/tmp/central-eu-clone/mail.tar.gz /var/spool/mail

tar -zcvpf /root/tmp/central-eu-clone/home.tar.gz /home

tar -zcvpf /root/tmp/central-eu-clone/openvpn.tar.gz /etc/openvpn



tar -zcvpf /root/tmp/central-eu-clone.tar.gz /root/tmp/central-eu-clone



