## postfix

### Good reads
https://www.cyberciti.biz/faq/howto-blacklist-reject-sender-email-address/

#### Base commands for most mail systems

  tail -f maillog |grep blocked
  tail  maillog |grep blocked
  cat maillog |grep Blocked
  
  /usr/local/lib/nagios/plugins/check_postfix_blocked.py -vvv -w 20 -c 35 2>&1 | grep wor

  /usr/local/lib/nagios/plugins/check_postfix_blocked.py -vvv -w 20 -c 35 2>&1 | grep block

  mailq |grep D75D711F2
  postcat -q D75D711F2

  cd /var/mail/
  cd /var/spool/
  cd postfix/
  cd deferred/

  postcat -q 1/173E11157 
  postqueue -p
  mailq

  tail -f /var/log//maillog
  tail -f /var/log//maillog |grep reject
  tail -f /var/log//maillog |grep connect

  zgrep -i 'earthlink' /var/log/maillog*
  postcat -q 065E71E1D

####read mail

postcat -q  messageid

#### look at queued messaages

postqueue -p

#### delete message from postfix queue

postsuper -d messageid



watch -d -n 1 'ls -lhart /var/spool/postfix/active'

and

watch 'netstat --program --numeric-hosts --numeric-ports --extend | grep -E ":25|postfix|smtp"'

For about 30 minutes and see no outgoing activity.


tail -f /var/log/maillog

