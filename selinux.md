## SELinux

### Good reads
https://opensource.com/article/18/7/sysadmin-guide-selinux
https://opensource.com/business/13/11/selinux-policy-guide
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/security-enhanced_linux/sect-security-enhanced_linux-working_with_selinux-selinux_contexts_labeling_files
https://wiki.gentoo.org/wiki/SELinux/Tutorials/Where_to_find_SELinux_permission_denial_details
https://www.golinuxhub.com/2014/05/how-to-track-all-successful-and-failed.html
https://access.redhat.com/articles/2191331
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/security-enhanced_linux/sect-security-enhanced_linux-troubleshooting-top_three_causes_of_problems
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html-single/selinux_users_and_administrators_guide/#sect-Security-Enhanced_Linux-Targeted_Policy-Confined_and_Unconfined_Users-sudo_Transition_and_SELinux_Roles

#### Cheat sheets

http://tojaj.com/selinux-cheat-sheet/

### Top 3 big causes of problems

Labelling
Context
Booleans
sudo

#### Basics

	getenforce

Show what mode SELinux is in: Disabled, Permissive or Enforcing. Switch SELinux to enforcing mode with ‘setenforce 1’.

	ls -Z

	ps aux _z

#### What does the context name mean

See above good reads documents

#### Set temporary selinux contexts to test

	chcon -t nrpe_var_run_t file.txt


```bash
# Super simple quick bash script for fun and profit
cmd explanation
cmd | -t=type | context_name | file

chcon -t nrpe_var_run_t name_of_file
```

#### Set permanent selinux contexts

	semanage fcontext -a -t lib_t -s system_u name_of_file
	restorecon -vF name_of_file

```bash
# Quick bash script if you need it for fun and profit
semanage fcontext -a -t lib_t -s system_u name_of_file
restorecon -vF name_of_file
```

#### Check selinux permission denial details

	grep AVC /var/log/audit/audit.log
	grep AVC /var/log/audit/audit.log|audit2why
	grep AVC /var/log/audit/audit.log|audit2allow -M updatesMar12019
	semodule -i updatesMar12019.pp

	ausearch -m AVC,USER_AVC,SELINUX_ERR,USER_SELINUX_ERR -i

Further reading: https://wiki.gentoo.org/wiki/SELinux/Tutorials/Where_to_find_SELinux_permission_denial_details 

### More advanced topics

#### List all files and directories contexts

	semanage fcontext -l

Should out put a large version of this

	/var/www/svn(/.*)?                                 all files          system_u:object_r:httpd_sys_rw_content_t:s0 
	/var/www/svn/conf(/.*)?                            all files          system_u:object_r:httpd_sys_content_t:s0 
	/var/www/svn/hooks(/.*)?                           all files          system_u:object_r:httpd_sys_script_exec_t:s0 
	/var/www/usage(/.*)?                               all files          system_u:object_r:webalizer_rw_content_t:s0 
	/var/www/wiki[0-9]?(/.*)?                          all files          system_u:object_r:mediawiki_rw_content_t:s0 
	/var/www/wiki[0-9]?\.php                           regular file       system_u:object_r:mediawiki_content_t:s0 
	/var/yp(/.*)?                                      all files          system_u:object_r:var_yp_t:s0 
	/vicepa                                            all files          system_u:object_r:afs_files_t:s0 
	/vicepb                                            all files          system_u:object_r:afs_files_t:s0 
	/vicepc                                            all files          system_u:object_r:afs_files_t:s0 


Search the audit log for recently denied events triggered by Apache (‘httpd’). Useful for debugging an application that might be running into SELinux related problems.

	ausearch -sv no --comm httpd

Labels on all files under /var/www/html if different from those mentioned above.

	restorecon -FvR /var/www/html Use this command to restore the default

	semanage fcontext -l | grep '/var/

www' View all SELinux rules that potentially apply to /var/www in the extensive SELinux docs.
Install the policycoreutils-python package with yum to get the ‘semanage’ command.
If you have a database on a separate server, you need to allow Apache to initiate network
connections, which SELinux denies by default. This is done by setting an SELinux boolean.

#### Booleans

	$ getsebool

	setsebool httpd_can_network_connect_db 1

Show all available SELinux boolean settings Tell SELinux to allow httpd to make connections to databases on other servers.
Use the -P flag to make permanent.