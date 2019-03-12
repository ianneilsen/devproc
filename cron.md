## cron

#### Links

Simple page to help visually set your cron times - https://crontab.guru 


#### edit a cron from a user account

crontab -e

### show all cron jobs

[root@host ~]# cat /var/spool/cron/*


[root@host ~]# ls /etc/cron.*


#### test your cron without waiting

You can force the crontab to run with following command:


run-parts /etc/cron.hourly
run-parts /etc/cron.daily




