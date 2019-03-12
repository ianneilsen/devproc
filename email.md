

#### find imap users from logs

cat /var/log/mail/* | grep imap-login:\ Login | sed -e 's/.*Login: user=<\(.*\)>, method=.*/\1/g' | sort | uniq
