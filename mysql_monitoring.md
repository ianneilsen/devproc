## mysql monitoring


	mysql> show status like 'Conn%';
	mysql> show status like '%onn%';
	show processlist;
	show full processlist;
	show variables;


	mysql> SHOW GLOBAL STATUS LIKE 'Aborted_connections';
	fix = mysql> SET GLOBAL connect_timeout = 10;

	netstat -nat |grep 3306

Use Apache jmeter to load test

Look for errors in phplog or mysql logs
such as ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)


## Warnings

check logs

	mysql> show warnings;

	mysql> SHOW VARIABLES LIKE 'max_error_count';

	mysql>  SELECT @@warning_count;

	ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head

	ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head

	mysqladmin proc