## Apache Log formats

## Good Links

{% embed url="https://httpd.apache.org/docs/2.4/mod/mod_log_config.html#logformat" %}

* https://httpd.apache.org/docs/2.4/mod/mod_log_config.html#logformat


{% hint style="info" %}
Log format
By default, the Apache log configuration file defines two print formats: combined format and common format. You can also create your own customized log print format as neede
{% endhint %}


#### Combined format:

	LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined

Common format:
------------------

	LogFormat "%h %l %u %t \"%r\" %>s %b" 

Customized format:
--------------------

```bash
LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" %D %f %k %p %q %R %T %I %O" customized
```


You need to specify the print format, log file path, and log name of the current log in the Apache log configuration file. For example, the following log configuration file indicates that combined print format is used, and the log path and name is displayed as /var/log/apache2/access_log.



Field description
==================

Format	Key name	Description
---------------------------------

* %a	client_addr	Client IP address.
* %A	local_addr	Local private IP address.
* %b	response_size_bytes	Size of response in bytes. When the size of response is null, this field is a hyphen (-).
* %B	response_bytes	Size of response in bytes. When the size of response is null, this field is a hyphen (-).
* %D	request_time_msec	Request time, in microseconds.
* %h	remote_addr	Remote hostname.
* %H	request_protocol_supple	Request protocol.
* %l	remote_ident	Client log name from identd.
* %m	request_method_supple	Request method.
* %p	remote_port	Server port.
* %P	child_process	Child process ID.
* %q	request_query	Query string. If no query string exists, this field is an empty string.
* "%r"	request	Request content, including the request method name, address, and HTTP protocol.
* %s	status	HTTP status code.
* %>s	status	Final HTTP status code.
* %f	filename	Filename.
* %k	keep_alive	Number of keepalive requests.
* %R	response_handler	Handler on the server.
* %t	time_local	Server time.
* %T	request_time_sec	Request time, in seconds.
* %u	remote_user	Client username.
* %U	request_uri_supple	Requested URL path. No query is included in the path.
* %v	server_name	Server name.
* %V	server_name_canonical	Server name conforming to the UseCanonicalName setting.
* %I	bytes_received	Number of bytes received by the server. You must enable the mod_logio module.
* %O	bytes_sent	Number of bytes sent by the server. You must enable the mod_logio module.
* "%{User-Agent}i"	http_user_agent	Client information.
* "%{Rererer}i"	http_referer	Source page.



Sample log
===============

192.168.1.2 - - [02/Feb/2016:17:44:13 +0800] "GET /favicon.ico HTTP/1.1" 404 209 "http://localhost/x1.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36" 

