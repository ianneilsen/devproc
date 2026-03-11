## cron

#### Links

Simple page to help visually set your cron times - https://crontab.guru 


#### edit a cron from a user account

```bash
crontab -e
```

### show all cron jobs

```bash
cat /var/spool/cron/*
ls /etc/cron.*
```

#### test your cron without waiting

You can force the crontab to run with following command:

```bash
run-parts /etc/cron.hourly
run-parts /etc/cron.daily
```




