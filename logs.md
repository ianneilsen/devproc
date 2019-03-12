## Logs and log examination

### Good Links

https://www.the-art-of-web.com/system/logs/
https://www.the-art-of-web.com/system/logs/


	awk '{print $9}' combined_log | sort | uniq -c | sort

#### who is hotlinking my images

	awk -F\" '($2 ~ /\.(jpg|gif)/ && $4 !~ /^http:\/\/www\.coastaltool\.com/){print $4}' combined_log | sort | uniq -c | sort

### logrotate

Keep in mind that global configuration specified in /etc/logrotate.conf will not apply, so if you do this you should ensure you specify all the options you want in the /etc/logrotate.d/[servicename] config file specifically.

You can try it out with -d to see what would happen:

	logrotate -df /etc/logrotate.d/nginx

Then you can run (using nginx as an example):

	logrotate -f /etc/logrotate.d/nginx

And the nginx logs alone will be rotated.

	logrotate -vf /etc/logrotate.conf
