## curl

Now we can download the test.php file from either the same machine, or our local
workstation:

	curl http://www.someapp.org/test.php

	curl http://localhost:80/someapp/api -v 

Fetch sent and received HTTP GET status, API response payload from the local host 

	curl https://localhost:443/someapp/api -v -F “arg1=foo” -F “arg2=bar” 

Fetch sent and received HTTPS POST status, API response payload from the local host

	$ host www.someapp.org 

Use the ‘host’ command to test DNS name resolution; you might need to run ‘yum -y install bind-utils’ for this command to work.
