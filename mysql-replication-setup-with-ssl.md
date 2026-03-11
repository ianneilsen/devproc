## mysql 5.7 replication setup with ssl

### Good reads

Link to ssl creation
https://blog.pythian.com/setting-up-mysql-encrypted-replication-on-mysql-5-7-with-gtid/
Enable replication on slave
https://www.howtoforge.com/how-to-set-up-mysql-database-replication-with-ssl-encryption-on-centos-5.4-p2/amp/
#### NOTES
If you want to use the SQL statement to set ssl you can, without using the my.cnf file
Check replication by creating new table then deleting or adding in new records and running a 'select' query
Check mysql logs. During day-to-day operations, you should place the mysql logs into rotation.

Links
https://www.google.com/amp/s/www.cyberciti.biz/faq/how-to-set-up-mariadb-master-slave-replication-with-ssl-on-ubuntu-linux/amp/
https://www.howtoforge.com/how-to-set-up-mysql-database-replication-with-ssl-encryption-on-centos-5.4-p2/amp/
https://www.percona.com/blog/2013/06/22/setting-up-mysql-ssl-and-secure-connections/
https://www.digitalocean.com/community/tutorials/how-to-set-up-master-slave-replication-in-mysql
https://dev.mysql.com/doc/refman/5.7/en/using-encrypted-connections.html
https://dev.mysql.com/doc/refman/5.7/en/replication-solutions-encrypted-connections.html
https://www.opsdash.com/blog/mysql-replication-howto.html

## No downtime mysql replication

https://plusbryan.com/mysql-replication-without-downtime
https://www.borfast.com/blog/2014/02/15/how-to-add-a-slave-to-a-mysql-replication-setup-with-no-downtime/
https://www.howtoforge.com/mysql_database_replication
https://serverfault.com/questions/220322/how-to-setup-mysql-replication-with-minimal-downtime
https://www.howtoforge.com/mysql_database_replication



### Is ssl already running on server?

	show variables like '%ssl%';

openssl req -x509 -sha256 -nodes -newkey rsa:2048 -keyout privateKey.key -out certificate.crt

#### Setup ssl certs keys

	openssl genrsa 2048 > ca-key.pem
	openssl req -new -x509 -nodes -key ca-key.pem > ca-cert.pem

#### Create the server and client keys off the car cert

Server

	openssl req -newkey rsa:2048 -nodes -keyout server-key.pem > server-req.pem
	openssl x509 -req -in server-req.pem -CA ca-cert.pem -CAkey ca-key.pem > server-cert.pem

Client

	openssl req -newkey rsa:2048 -nodes -keyout client-key.pem > client-req.pem
	openssl x509 -req -in client-req.pem -CA ca-cert.pem -CAkey ca-key.pem > client-cert.pem

### Setup users on both servers, master and slave

When setting up a replication user, ensure you always use ssl. If you don't connection sin MySQL will fall back to non-ssl. There are MySQL version differences
on whether you set in the my.cnf file or via the sql statement. It's always better to er on the side of safety... better safe than sorry!

	mysql -u root -p

Master server - the line require ssl ensure that this new user can only connect via ssl and not drop back.

	CREATE USER 'replication'@'<slave_ip>' IDENTIFIED BY '<password>' REQUIRE SSL;
	GRANT REPLICATION SLAVE ON *.* TO 'replication'@'<slave_ip>';
	FLUSH PRIVILEGES;
	show grants;

Slave server

	create user 'replication'@'%'  IDENTIFIED BY '<password>';
	create database db-name;
	grant replication slave on *.* to 'replication_user'@'%';
	FLUSH PRIVILEGES;
	show grants;

### Setup firewall

	iptables -A input -s slave_server_ip(or hostname) -dport 3306 -j ACCEPT

### If you dont have a log directory you will need to set this up and add appropiate permissions

	cd /var/log/mysql
	mkdir /var/log/mysql
	chown mysql:mysql /var/log/mysql

### Find and modify MySQL conf - my.cnf

You may have to search for which my.cnf file you are using. Whether this is mariadb, mysql native or percona mysql.

========Master Conf start========

==start==

	server-id = 1
	log_bin = /var/log/mysql/mysql-bin.log
	expire_logs_days = 10
	max_binlog_size = 100M
	binlog_do_db = <database_name>

	ssl-ca=/var/lib/mysql/ca.pem
	ssl-cert=/var/lib/mysql/server-cert.pem
	ssl-key=/var/lib/mysql/server-key.pem

==end==

	other confs

	ssl
	ssl-ca=/etc/mysql/newcerts/ca-cert.pem
	ssl-cert=/etc/mysql/newcerts/server-cert.pem
	ssl-key=/etc/mysql/newcerts/server-key.pem

	relay-log = mysql-relay-bin
	relay-log-index = mysql-relay-bin.index


=======Master Conf end===========

Restart mysql master service

	systemctl restart mysql.service


### Prepare data to export and import

On master - Do the following in a tmux session, cause we need another window to export db while it's locked

	USE <database_name>;
	FLUSH TABLES WITH READ LOCK;
	SHOW MASTER STATUS;

Output on master should look like the following. Note down the FILE and POSITION. YOu will need this for the slave.

	mysql> SHOW MASTER STATUS;
	+------------------+----------+---------------+------------------+-------------------+
	| File             | Position | Binlog_Do_DB  | Binlog_Ignore_DB | Executed_Gtid_Set |
	+------------------+----------+---------------+------------------+-------------------+
	| mysql-bin.000001 |      154 | <database_name> |                  |                   |
	+------------------+----------+---------------+------------------+-------------------+
	1 row in set (0.00 sec)

#### Export database from master server

	cd /tmp
	mysqldump -u root -p <database_name> > /root/tmp/<database_name>_snapshot.sql

	scp <database_name>_snapshot.sql root@<slave_ip>:/root/tmp/

	UNLOCK TABLES;
	quit

#### Import database to slave server

	CREATE DATABASE <database_name>;
	mysql -u root -p <database_name> < /root/tmp/<database_name>_snapshot.sql -v
	mysql -u root -p
	use database <database_name>;

#### Modify slave configuration

======Slave conf start=====

example 1
--------------
	server-id = 2
	master-host = <master_ip>
	master-connect-retry = 60
	master-user = replication
	master-password = <password>
	replicate-do-db = <database_name>
	log-bin = /var/log/mysql/mysql-bin.log
	log_error = /var/log/mysql/error_slave.log

	[client]
	ssl-ca=/var/lib/mysql/mysql_slave/ca.pem
	ssl-cert=/var/lib/mysql/mysql_slave/client-cert.pem
	ssl-key=/var/lib/mysql/mysql_slave/client-key.pem


example 2
--------------
	server-id = 2
	replicate-do-db = <database_name>
	log-bin = /var/log/mysql/mysql-bin.log
	log_error = /var/log/mysql/error_slave.log

	[client]
	ssl-ca=/var/lib/mysql/mysql_slave/ca.pem
	ssl-cert=/var/lib/mysql/mysql_slave/client-cert.pem
	ssl-key=/var/lib/mysql/mysql_slave/client-key.pem

	==end==
	relay-log = /var/log/mysql/mysql-relay-bin

	Might put this in the sql statement

	ssl
	ssl-ca=/var/lib/mysql/mysql/ca.pem
	ssl-cert=/var/lib/mysql/mysql/client-cert.pem
	ssl-key=/var/lib/mysql/mysql/client-key.pem

====slave conf end====

Then restart mysqld slave service

	systemctl restart mysqld.service

### Check ssl connect from slave

Verify ssl connection and firewall
The following command should fail as ssl 3 is not supported and configured to use:

	$ openssl s_client -connect <master_ip>:3306 -ssl3

	 mysql -h <master_ip> -u replicationUser -p --ssl-ca=/var/lib/mysql/ssl-certs/ca.pem --ssl-cert=/var/lib/mysql/ssl-certs/client-cert.pem --ssl-key=/var/lib/mysql/ssl-certs/client-key.pem

Check for TLS v 1/1.1/1.2:

	$ openssl s_client -connect <master_ip>:3306 -tls1
	$ openssl s_client -connect <master_ip>:3306 -tls1_1
	$ openssl s_client -connect <master_ip>:3306 -tls1_2

### Enable replication on slave server to master - START it ALL off

First check that ssl is working and that you can connect to master server with user and database.
Second enable replication. At this point you will need the information from the master server, such as binlog file and log position to enter the sql statement.

	mysql -u root -p
	use database <database_name>;
	stop slave;

	CHANGE MASTER TO MASTER_HOST='<master_ip>', MASTER_USER='replication_user_name', MASTER_PASSWORD='<password>', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=154 MASTER_SSL=1, MASTER_SSL_CAPATH = '/var/lib/mysql/mysql_slave/', MASTER_SSL_CA = 'ca.pem', MASTER_SSL_CERT = 'client-cert.pem', MASTER_SSL_KEY = 'client-key.pem';

	start slave;
	SHOW SLAVE STATUS\G


	CHANGE MASTER TO MASTER_HOST='<master_ip>', MASTER_USER='replication_user_name', MASTER_PASSWORD='<password>', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=154 MASTER_SSL=1, TER_SSL_CAPATH = '/var/lib/mysql/mysql_slave/',
	MASTER_SSL_CA = 'ca.pem',
    MASTER_SSL_CERT = 'client-cert.pem',
    MASTER_SSL_KEY = 'client-key.pem';


	create user 'replicationUser'@'<slave_ip>' identified by '<password>' REQUIRE SSL;

	openssl s_client example.com:3306 -CAfile /var/lib/mysql/mysql_slave/ca.pem -debug -showcerts

	openssl s_client -connect example.com:3306 -CAfile /var/lib/mysql/mysql_slave/ca.pem -debug -showcerts

	mysql -u replicationUser -p -sss -e '\s'|grep SSL

	mysql -u replicationUser -p -h <master_ip> -sss -e '\s'|grep SSL

	mysql -u root -p db-name < /root/tmp/db-name_snapshot.sql -v

	mysql -u root -p db-name < /root/tmp/db-name_snapshot.sql -v

	mysql -u root db-name < /root/tmp/db-name_snapshot.sql -v

	tmux new -s MYmysql

	mysql -u root <database_name> < /root/tmp/db-name_snapshot.sql -v

test ssl connection
=======================

mysql -h <master_ip> -u replicationUser -p --ssl-ca=/var/lib/mysql/ssl-certs/ca.pem --ssl-cert=/var/lib/mysql/ssl-certs/client-cert.pem --ssl-key=/var/lib/mysql/ssl-certs/client-key.pem

mysql -h <master_ip> -u replicationUser -p --ssl=0


mysql> show master status;
+------------------+----------+---------------+------------------+-------------------+
| File             | Position | Binlog_Do_DB  | Binlog_Ignore_DB | Executed_Gtid_Set |
+------------------+----------+---------------+------------------+-------------------+
| mysql-bin.000002 |      154 | <database_name> |                  |                   |
+------------------+----------+---------------+------------------+-------------------+
1 row in set (0.00 sec)
