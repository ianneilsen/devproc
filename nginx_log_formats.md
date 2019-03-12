## nginx log formats


The Nginx log format and directory are generally in the configuration file /etc/nginx/nginx.conf.

Nginx log format
The log configuration file defines the print format of Nginx logs, that is, the main format:
log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                 '$request_time $request_length '
                 '$status $body_bytes_sent "$http_referer" '
                 '"$http_user_agent"';
The declaration uses the main log format and the written file name.

access_log /var/logs/nginx/access.log main
Field Description
Field name 	Definition
remoteaddr	The IP address of the client.
remote_user 	The username of the client.
request 	The requested URL and HTTP protocol.
status	The request status.
bodybytessent	The number of bytes (not including the size of the response header) sent to the client. The total number of bytes for this variable is the same as that sent to the client by bytes_sent in modlogconfig of the Apache module.
connection	The connection serial number.
connection_requests 	The number of requests received by using a connection.
msec	The log write time, which is  which is measured in seconds and precise to milliseconds.
pipe	Whether or not requests are sent by using the HTTP pipeline.  p indicates requests are sent by using the HTTP pipeline. Otherwise, the value is . . 
httpreferer	 Web page link from which the access is directed.
“http_user_agent”	Information about the browser on the client. http_user_agent must be enclosed in double quotation marks.
requestlength	The length of a request, including the request line,  request header, and request body. 
Request_time	The request processing time, which is measured in seconds and precise to milliseconds.  The time starts when the first byte is sent to the client and ends when the logs are written after the last character is sent to the client. 
[$time_local]	he local time in the general log format. This variable must be enclosed in brackets.
Log sample
192.168.1.2 - - [10/Jul/2015:15:51:09 +0800] "GET /ubuntu.iso HTTP/1.0" 0.000 129 404 168 "-" "Wget/1.11.4 Red Hat modified" 

