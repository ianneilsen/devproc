#### Find and inspect what linux users are doing

who
===============

```bash
who -la
```
when you can see a tty session open and pts use `ps` to inspect process

```bash
ps -ft pts/6
or
# pkill -9 -t pts/0
```

command is another way if it is installed

# finger

```bash
finger
```
# last

```bash
last
```

# w

```bash
w
```

Network
===========

```bash
netstat -anp
lsof -V
ps -ef
netstat -rn
lsmod
```

ls
===============
privelaged directories, look for hidden directories, weird permissions, atrributes or dates and times
directories dont match up to a standard install, directories contain weird files or other directories
directories are going to be scattered

```bash
ls -lap /dir

ls -lap /bin
```

Good dirs to search, commmon grounds.
```bash
/tmp, 
/var/tmp
/dev
/dev/shm
/bin
/sbin
/usr/bin
/usr/sbin
/lib
/usr/lib
/etc
/var
/var/log
/var/spool/cron
/var/www
```

directories examples 

```bash
. .
...
% )'
```

Files
===========

```bash
	find / -name \*.bin

	find / -name \*.exe
```

Create a timeline of all files on the system

```bash
	find / -type f -printf "%P,%A+,%T+,%C+,%u,%g,%M,%s\n"
```

Processes
=====================

Process tree:

```bash
	ps -auxwf
	pstree -Aup
```

Open network ports or raw sockets:

```bash
	netstat -nalp
	netstat -plant
	ss -a -e -i
	lsof [many options]
```

Deleted binaries still running:

```bash
	ls -alR /proc/*/exe 2> /dev/null | grep deleted
```

Process command name/cmdline:

```bash
	strings /proc/<PID>/comm
	strings /proc/<PID>/cmdline
```

Real process path:

```bash
	ls -al /proc/<PID>/exe
```

Process environment:

```bash	
	strings /proc/<PID>/environ
```

Process working directory:

```bash
	ls -alR /proc/*/cwd
```

Process running from tmp, dev dirs:

```bash
	ls -alR /proc/*/cwd 2> /dev/null | grep tmp
	ls -alR /proc/*/cwd 2> /dev/null | grep dev
```

lsattr - immutable flags
===============
Anything with an i or immtable flag on files directories. When you find  directories you will start to find suspcious files
often used to maintain persistence - so you need to remove immutable flags to remove dir or file. Its not typical because its hard to remove with normal commands

tampered or missing auditd logs. files that are not what they clam to be or are out of place binaries that are modifed or in strange locations
when you start to find weird directories you will start to find weird files

```bash
	lsattr -a /dir
```

Immutable files and directories:

```bash
	lsattr / -R 2> /dev/null | grep "\----i"
```

Find SUID/SGID files:

```bash
	find / -type f \( -perm -04000 -o -perm -02000 \) -exec ls -lg {} \;
```

Files/dirs with no user/group name:

```bash
	find / \( -nouser -o -nogroup \) -exec ls -lg {} \;
```

Find executables anywhere, /tmp, etc.:

```bash
	find / -type f -exec file -p '{}' \; | grep ELF
```

Persistence areas:

```bash
	/etc/rc.local, /etc/initd, /etc/rc*.d, /etc/modules, /etc/cron*, /var/spool/cron/*
```

Package commands to find changed files:

```bash
	rpm -Va | grep ^..5.
	debsums -c
```


User check
===============

```bash
awk -F: ''$3 == 0 && $1 !~ /root/ {print $1}'' /etc/passwd
```

History files linked to /dev/null:

```bash
	ls -alR / 2> /dev/null | grep .*history | grep null
```

Find no user or nogroup

```bash
find / -nouser

find / -nogroup
```

auditd
===============
audit logs are a high value target it is hit so often. How often do you look at logs as a system admin. Using a log solution helps with

logs - hot items
===============
Look for zero bites, times and dates are they all the same, are compressed logs from log rotate at zero lengths - shouldnt really be the case
look at btmp. look at kernel logs

```bash
wtmp
lastlog
btmp
utmp
/log*
```

tmp
===============
ofen used as scratch pad. Tools break, tools fail

```bash
ll -trap /tmp
```

last and lastb
===============

```bash
last
lastb
```

tmp directory
===============

look for odd files
look for commands in the tmp

User tmps
===============
Why is there a gap in the file
if you have blanks, someone could have wipe logins

utmp = All current logins

```bash
	utmpdump < /var/run/utmp

[6] [00706] [tyS0] [LOGIN   ] [ttyS0       ] [                    ] [0.0.0.0        ] [Wed Aug 15 06:06:33 2018 UTC]
[6] [00705] [tty1] [LOGIN   ] [tty1        ] [                    ] [0.0.0.0        ] [Wed Aug 15 06:06:33 2018 UTC]
[8] [01328] [ts/1] [        ] [pts/1       ] [                    ] [64.64.64.64   ] [Wed Aug 15 10:06:35 2018 UTC]


	tomcat   ssh:notty    64.64.64.64      Sun Aug 12 19:10 - 19:10  (00:00)    
	oracle   ssh:notty    64.64.64.64      Sun Aug 12 19:09 - 19:09  (00:00)    

	        ssh:notty    64.64.64.64      Sun Aug 12 19:08 - 19:08  (00:00)    
	boss     ssh:notty    64.64.64.64      Sun Aug 12 19:08 - 19:08  (00:00)   

btmp = All Bad logins

	utmpdump < /var/log/btmp

wtmp = All valid past logins

	utmpdump < /var/log/wtmp 
```

Find files/confs
===============

Find files especially confs, which may have been modified away from the base configuration

```bash
rpm -Va |grep ^..5.
```

and run this also

```bash
rpm -qa | rpm -Va
```

check for ??
```bash
rpm -Va | grep ''^.M''
```

Ubuntu/Debian not loaded by default

```bash
debsums -c
```

Nologin
=============

if you see `nologin` has been altered - may equal someone has edited a different bash login
attention to detail is important

netstat, ss and lsof
===============
look for raw sockets, strange port numbers

```bash
# netstat -nalp
# netstat -plant
# netstat -tulpn

# ss -tlpa
# ss -a -e -i

# lsof
# lsof |wc -l
```

ps
===============

```bash
# ps -auxwf
```

high process id's which means it started late in the system where are processes running from - like running out tmp, root, dev

proc
===============
proc is your saviour alot of the times. Deletd processes after starting so it works and binary is gone so its hard to search
any hashing techniques or file changes is now gone from your system

look for deletd files or process files, high process ids, binary deleted starting, you can check what file is doing

```bash
# ls -al /proc/22551
```

strings
===============
Do not run strace on binary - strace is no good because it executes the binary. Can show game plan on binary

```bash
# strings /dev/binary
```

look for 
===============
x11 on a bare minimal server??


enable inotifier
enable auditd
hash bang you file systems
run a virtual machine with all your tools on it to use as a comparison against your production system
run antivirus
run a intrusion detection system
run selinux - spend the time to set it up
sysadmins - rotate you ssh keys regularly
stagger your cron jobs especially if using inotify, auditd or ossec

quick after checks
===============

There must be no .shosts files on the system.

There must be no shosts.equiv files on the system.


All files and directories must have a valid owner."
command: 

```bash
# find / -xdev -fstype xfs -nouser
```

All files and directories must have a valid group owner."
command: 

```bash
# find / -xdev -fstype xfs -nogroup
```

Find out all files that are not owned by any user:

```bash
# find / -nouser
```

Find out all files that are not owned by any group:

```bash
# find / -nogroup
```

For example in real life on busy clustered hosting server some time we remove 5-10 users and for security reasons you need to find out all files are not owned by any user or group then you can type command:

```bash
# find / -nogroup -nouse
```
\n