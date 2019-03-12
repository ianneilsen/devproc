mysql replication setuip from mysql 5.1 to 5.6
===============================================

## good links
https://www.stephenrlang.com/2016/08/setting-up-mysql-master-slave-replication-with-xtrabackup/
https://www.digitalocean.com/community/tutorials/how-to-set-up-master-slave-replication-in-mysql
https://www.digitalocean.com/community/tutorials/how-to-set-up-mysql-master-master-replication
https://www.opsdash.com/blog/mysql-replication-howto.html
https://www.schalley.eu/2017/01/16/setting-up-mysql-replication-with-existing-data-master-slave/
https://support.rackspace.com/how-to/set-up-mysql-master-slave-replication/
https://severalnines.com/blog/top-mistakes-avoid-mysql-replication
https://www.stephenrlang.com/2016/08/setting-up-mysql-master-slave-replication-with-xtrabackup/

#### questions

will myisam still work - needs checking
what happens if we need to convert to innodb on tables
plugins are installed - will they all be supported in gce sql
binlog issues
permission issues between percona mysql and gce sql

#### checks to perform

#### check for old my.cnf formats

	egrep -ni 'innodb_adaptive_checkpoint|suppress_log_warning_1592|innodb_pass_corrupt_table|innodb_expand_import|innodb_auto_lru_dump|log_slow_timestamp_every|slow_query_log_microseconds_timestamp|use_global_log_slow_control|enable_query_response_time_stats|innodb_buffer_pool_shm_key|innodb_buffer_pool_shm_checksum' /etc/my.cnf

#### check symlink space issues

	du -sch /var/lib/mysql/ $(for i in $(find /var/lib/mysql/ -type l); do readlink $i; done)

#### check in memory

	select concat('ALTER TABLE `',table_schema,'`.`',table_name,'` ENGINE=INNODB;') from information_schema.tables where engine='memory' and table_schema not in ('information_schema','performance_schema');

#### show all plugins

	show plugins;

#### show all tables engine type

	select TABLE_NAME, ENGINE from information_schema.TABLES where TABLE_SCHEMA='db-name';

#### Basic Steps

dump master server msyql schema
dump master sever data
dump master server privelages
create a replication user with all privelages on master/slave
setup master - slave replication in config files

    FLUSH TABLES WITH READ LOCK;

execute full import backup to slave

    unlock tables;

On the master
----------------
You 

    FLUSH TABLES WITH READ LOCK; 
On the database you want to replicate

    SHOW MASTER STATUS

* and copy the file name and the position
* Excute a full backup to the database you want to replicate
* Then release the tables with 

    UNLOCK TABLES;

On slave
-------------

* Restore the database
* Excute this 
 
        CHANGE MASTER TO MASTER_HOST = 'masterhost', MASTER_USER = 'masteruser', MASTER_PASSWORD = 'masterpass', MASTER_LOG_FILE = 'filename', MASTER_LOG_POS = 'position';

* Then start slave;


Upgrading mysql from 5.1 to 5.6
======================================
https://mysqlserverteam.com/upgrading-directly-from-mysql-5-0-to-5-6-with-mysqldump/

https://dba.stackexchange.com/questions/111798/upgrading-the-mysql-server-from-5-1-to-5-6#111937

verifying tables
===============

pt-table-checksum

pt-label-sync

Issues
==========
Temporary Table Drops and Binlogging on GTID-Enabled Server

You are correct, however it is recommended that when upgrading from 5.1 to 5.5 that you export (mysqldump) and re-import your data into the 5.5 instance and then run mysql_upgrade; this is the cleanest method.


