mysql
==========

#### Good Links

Document to mysql https://dev.mysql.com/doc/refman/5.7/en/show-status.html

#### Quick install

Install percona mysql

	yum install https://repo.percona.com/yum/percona-release-latest.noarch.rpm
	yum install Percona-Server-server-


#### Show database details

Table schema
----------------------

	show columns from mytable from mydb;

	show columns from mydb.mytable;

Database schema
-----------------------
Database info schema types
----------------------------

#### Show sql mode

https://dev.mysql.com/doc/refman/5.7/en/sql-mode.html
https://coursesweb.net/forum/mysql-error-sql-mode-timestamp-implicit-deprecated-t265.htm

#### Users

https://dev.mysql.com/doc/refman/5.7/en/show-grants.html

	select * from mysql.user;

	SELECT User, Host, Password FROM mysql.user;

	desc mysql.user;


#### mysql export and import

mysqldump
---------
data only:

https://stackoverflow.com/questions/5109993/mysqldump-data-only

schema only:

large tables:

export database or databases
----------------------------

	mysqldump -v -u root --all-databases > datadump.sql

	mysqldump --databases database_one database_two > two_databases.sql

	mysqldump -u root -p --opt --all-databases > alldb.sql

	mysqldump -u root -p --all-databases --skip-lock-tables > alldb.sql

	mysqldump -u root --no-data > nodata-justschema.sql

import databases
---------------------

	mysql -v -u database_user -p database_name < database_backup_file.sql --show-warnings

#### Show variables

show database variables for your database
-------------------------------------------
https://www.percona.com/doc/percona-xtradb-cluster/LATEST/howtos/ubuntu_howto.html

	show variables like 'character_set%';


#### Create users and databases;
Create database
Create user

	create database db-name;
	CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
	GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
 

Grant privileges to users
---------------------------
Change localhost to remote ip address if you require users to login via port 3306 remotely.

	GRANT ALL PRIVILEGES ON database.table TO 'user'@'localhost';


Password changes or adds
-------------------------------
https://www.percona.com/blog/2016/03/16/change-user-password-in-mysql-5-7-with-plugin-auth_socket/

Older mysql
-------------

	UPDATE mysql.user SET Password=PASSWORD('#31#-u1z8-X7X5') WHERE USER='nrpe' AND Host='localhost';

	alter user 'nrpe'@'localhost' identified by '#31#-u1z8-X7X5';

New mysql
---------

	ALTER USER 'trippy'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

	GRANT ALL PRIVILEGES ON mydb.* TO 'myuser'@'%' WITH GRANT OPTION;
	GRANT ALL PRIVILEGES ON databasename.* TO 'myuser'@'localhost' WITH GRANT OPTION;

	GRANT ALL PRIVILEGES ON `db-name`.* TO 'trippy'@'localhost' WITH GRANT OPTION;
	FLUSH PRIVILEGES;
	SHOW GRANTS FOR 'db-name'@'localhost';


#### More show statements

Schema and Processes
-------------------------

	SELECT id FROM information_schema.processlist WHERE command <> 'Sleep' AND info NOT LIKE '%PROCESSLIST%' AND command <> 'Killed' AND info LIKE '%EXPLAIN';


	Large attachments in database
------------------------------------

--hex-blob is good for tables with blob based attachments to get the correct utf8 char set.


Query checking

	SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST WHERE COMMAND != 'Sleep';

	SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST WHERE COMMAND != 'Sleep' AND TIME >= 5;

	SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST WHERE COMMAND != 'Sleep' AND INFO LIKE '%UPDATE %';

	mysql> show processlist\G

explain for connection 9 G

	mysql>show processlist;

mysql> kill "number from first col";

KILL QUERY **Id** where Id is connection id from show processlist

	mysqladmin proc stat

#### Large files or db's in mysql

If you have large tables and large attachments it can help to expand the max_allowed_packet size
----------------------------------------------------------------------------------
https://stackoverflow.com/questions/8062496/how-to-change-max-allowed-packet-size
https://stackoverflow.com/questions/10474922/error-2006-hy000-mysql-server-has-gone-away

Dealing with large tables
--------------------------------
http://forums.whirlpool.net.au/archive/2068357

Using Amazon Replicas
---------------------------
https://aws.amazon.com/rds/pricing/
https://support.symantec.com/en_US/article.HOWTO16962.html
