## postgres

#### Good Links

https://www.cheatography.com/squixy/cheat-sheets/postgresql-interactive-terminal-commands/

#### Postfix postgresql

	insert into tables values ('value1','value1','value1','value1',now(),'America/New_York');

#### Create database, user and add permissions

https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e

#### Users

https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e

## stats

```ruby
postgres=# select state, count(*) from pg_stat_activity group by 1;
 state  | count
--------+-------
 active |     6
 idle   |  1369
(2 rows)

postgres=# select client_addr, count(*) from pg_stat_activity group by 1;
 client_addr | count
-------------+-------
 192.0.2.10  |  1285
 192.0.2.11  |    37
 192.0.2.20  |    26
             |    27
(4 rows)

postgres=# select usename, count(*) from pg_stat_activity group by 1;
  usename  | count
-----------+-------
 bucardo   |    48
 user1     |  1322
 postgres  |     5
(3 rows)

postgres=# select count(*) from pg_stat_activity where state = 'idle' and state_change < now() - interval '1 hour';
 count
-------
  1236
(1 row)

postgres=# select count(*) from pg_stat_activity where state = 'idle' and state_change < now() - interval '2 hours';
 count
-------
   914
(1 row)

postgres=# select count(*) from pg_stat_activity where state = 'idle' and state_change < now() - interval '3 hours';
 count
-------
   255
(1 row)
```