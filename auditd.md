## auditd

### good links

https://www.systutorials.com/docs/linux/man/8-aureport/
https://www.cyberciti.biz/tips/linux-audit-files-to-see-who-made-changes-to-a-file.html 
https://highon.coffee/blog/security-harden-centos-7/#auditd-rules-etcauditauditrules

https://www.systutorials.com/docs/linux/man/8-aureport/

https://www.golinuxhub.com/2013/05/using-audit-in-linux-to-track-system.html

https://www.digitalocean.com/community/tutorials/how-to-use-the-linux-auditing-system-on-centos-7

#### find failed logins auditd

`ausearch -m USER_LOGIN -sv no`


#### find modifications to user,groups and roles

`ausearch -m ADD_USER,DEL_USER,USER_CHAUTHTOK,ADD_GROUP,DEL_GROUP,CHGRP_ID,ROLE_ASSIGN,ROLE_REMOVE  -i`

#### report

`aureport -x --summary`

#### failed report

`aureport --failed`

#### rpeort on sys calls and user names

`aureport -f -i`


#### trace the use of a command

`autrace /bin/ssh`

outsputs id

`ausearch -i -p 28587`

to summarise

`ausearch -p 28587 --raw |aureport -f -i`


#### aureport


Summary of all audit rules

`aureport -k`

or

`aureport -k -i`


report attempt at authentications
`aureport -au`

show summary of failed
`aureport --failed`

#### using date and time in aureports

https://www.tecmint.com/create-reports-from-audit-logs-using-aureport-on-centos-rhel/

`aureport -ts 09/19/2017 15:20:00 -te now --summary -i` 

OR

`aureport -ts yesterday -te now --summary -i`


