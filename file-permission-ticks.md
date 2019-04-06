## File permissions linux/unix


#### Just notes

Generally, files in /var/www/html are owned by apache.In a dev environment, you might want to make those files owned by apache and a developer group. Here are some
commands that are useful to make that a reality.

	chown apache:developers test.php 

Change ownership of test.php to “apache” and the “developers” group. (You can only change ownership of a file to another user
if you are the superuser, “root”.)

	chmod u+rw,g+rw,o+r test.php 

Change the mode of test.php to allow owner (u) and users in the group (g) to read and write (+rw) it, and the rest of the world (o)
to just read (+r) it.

	chmod g+rw test.php 

Allow users in the group of test.php to read and write it

	chown -R :developers /var/www/html 

Change ownership of /var/www/html and all files in that directory to the developers
group.

	chmod g+s /var/www/html 

Special command to make sure that all files created in /var/www/html are owned by the group that own /var/www/html; it sets to
so-called sticky bit.

Maybe you have a script that you want to use on that server, too. You’ll need to make it executable first:

	chmod 755 somescript 

Allow the owner of somescript to read, write and execute it, and the rest of the world to just read and execute it.

	chmod +x somefile 

Allow execution of somefile
