#!/bin/bash

# quick sanity checks

# show me all cron jobs
for user in $(cut -f1 -d: /etc/passwd); do echo $user; crontab -u $user -l; done

cat cron.*/

tail -n 1000 /var/spool/cron/*


print > cron

# show me all important mysql status'
mysql
show session status;
show global status;
show processlist;

show status;
show status like '%Key%';
show status like '%Thread%';
show status like '%Connected%';

SELECT * FROM INFORMATION_SCHEMA.STATISTICS;

mytop

print > mysql

# show me important network connections
netstat -at

watch -n1 lsof -i TCP:80,443
lsof -i TCP:80,443

print > network

# show me important log entries and counts


print > logs

# show my important postgresql status'


print > postgresql

# show memory usage


print memory

# show cpu usage


print cpu

# selinux

## auditd

auditctl -l

tail -5 /var/log/audit/audit.log

## ausearch

ausearch -m USER_LOGIN -sv no

ausearch -ua root

ausearch -m ADD_USER,DEL_USER,USER_CHAUTHTOK,ADD_GROUP,DEL_GROUP,CHGRP_ID,ROLE_ASSIGN,ROLE_REMOVE  -i


# apache

apachetop


# disk


iotop

# network


iftop


