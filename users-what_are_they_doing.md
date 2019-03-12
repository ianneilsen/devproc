#### Find and inspect what linux users are doing

who
===============

# who -la
when you can see a tty session open and pts use `ps` to inspect process

# ps -ft pts/6
or
# pkill -9 -t pts/0

command is another way if it is installed
# finger 
# last

# w

ls
===============
privelaged directories, look for hidden directories, weird permissions, atrributes or dates and times
directories dont match up to a standard install, directories contain weird files or other directories
directories are going to be scattered

# ls -lap /dir

# ls -lap /bin

Good dirs to search, commmon grounds.
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

directories examples 
. .
...
% )'


lsattr - immutable flags
===============
Anything with an i or immtable flag on files directories. When you find  directories you will start to find suspcious files
often used to maintain persistence - so you need to remove immutable flags to remove dir or file. Its not typical because its hard to remove with normal commands

tampered or missing auditd logs. files that are not what they clam to be or are out of place binaries that are modifed or in strange locations
when you start to find weird directories you will start to find weird files

# lsattr -a /dir

User check
===============

# awk -F: ''$3 == 0 && $1 !~ /root/ {print $1}'' /etc/passwd

auditd
===============
audit logs are a high value target it is hit so often. How often do you look at logs as a system admin. Using a log solution helps with

logs - hot items
===============
Look for zero bites, times and dates are they all the same, are compressed logs from log rotate at zero lengths - shouldnt really be the case
look at btmp. look at kernel logs

wtmp
lastlog
btmp
utmp
/log*

tmp
===============
ofen used as scratch pad. Tools break, tools fail

# ll -trap /tmp

last and lastb
===============

# last
# lastb

tmp directory
===============

look for odd files
look for commands in the tmp

User tmps
===============

# utmpdump < /var/run/utmp

[6] [00706] [tyS0] [LOGIN   ] [ttyS0       ] [                    ] [0.0.0.0        ] [Wed Aug 15 06:06:33 2018 UTC]
[6] [00705] [tty1] [LOGIN   ] [tty1        ] [                    ] [0.0.0.0        ] [Wed Aug 15 06:06:33 2018 UTC]
[8] [01328] [ts/1] [        ] [pts/1       ] [                    ] [64.64.64.64   ] [Wed Aug 15 10:06:35 2018 UTC]


look at and understand your process id types

Why is there a gap in the file
if you have blanks, someone could have wipe logins

	tomcat   ssh:notty    64.64.64.64      Sun Aug 12 19:10 - 19:10  (00:00)    
	oracle   ssh:notty    64.64.64.64      Sun Aug 12 19:09 - 19:09  (00:00)    

	        ssh:notty    64.64.64.64      Sun Aug 12 19:08 - 19:08  (00:00)    
	boss     ssh:notty    64.64.64.64      Sun Aug 12 19:08 - 19:08  (00:00)   

# utmpdump < /var/log/btmp

[6] [12658] [    ] [csgoserver] [ssh:notty   ] [64.64.64.64      ] [64.64.64.64 ] [Tue Aug 21 22:04:57 2018 UTC]
[6] [14456] [    ] [admin   ] [ssh:notty   ] [64.64.64.64       ] [64.64.64.64  ] [Wed Aug 22 00:02:14 2018 UTC]
[6] [10786] [    ] [user    ] [ssh:notty   ] [64.64.64.64       ] [164.64.64.64  ] [Wed Aug 22 00:34:44 2018 UTC]
[6] [03507] [    ] [0       ] [ssh:notty   ] [64.64.64.64       ] [64.64.64.64  ] [Wed Aug 22 01:45:26 2018 UTC]
[6] [16456] [    ] [22      ] [ssh:notty   ] [64.64.64.64       ] [64.64.64.64  ] [Wed Aug 22 02:01:10 2018 UTC]

# utmpdump < /var/log/wtmp 

Utmp dump of /dev/stdin
[5] [00687] [tty1] [        ] [tty1        ] [                    ] [0.0.0.0        ] [Wed Aug 15 21:39:31 2018 EDT]
[6] [00687] [tty1] [LOGIN   ] [tty1        ] [                    ] [0.0.0.0        ] [Wed Aug 15 21:39:31 2018 EDT]
[7] [00687] [tty1] [root    ] [tty1        ] [                    ] [0.0.0.0        ] [Wed Aug 15 21:41:15 2018 EDT]
[8] [00687] [tty1] [        ] [tty1        ] [                    ] [0.0.0.0        ] [Wed Aug 15 21:44:32 2018 EDT]
[1] [00000] [~~  ] [shutdown] [~           ] [3.10.0-862.el7.x86_64] [0.0.0.0        ] [Wed Aug 15 21:44:34 2018 EDT]
[2] [00000] [~~  ] [reboot  ] [~           ] [3.10.0-862.11.6.el7.x86_64] [0.0.0.0        ] [Wed Aug 15 21:44:52 2018 EDT]
[1] [00051] [~~  ] [runlevel] [~           ] [3.10.0-862.11.6.el7.x86_64] [0.0.0.0        ] [Wed Aug 15 21:44:54 2018 EDT]



Find files/confs
===============

Find files especially confs, which may have been modified away from the base configuration

# rpm -Va |grep ^..5.

and run this also

# rpm -qa | rpm -Va

check for ??
# rpm -Va | grep ''^.M''


Ubuntu/Debian not loaded by default

# debsums -c

Nologin
=============

if you see `nologin` has been altered - may equal someone has edited a different bash login
attention to detail is important

netstat, ss and lsof
===============
look for raw sockets, strange port numbers

# netstat -nalp
# netstat -plant
# netstat -tulpn

# ss -tlpa
# ss -a -e -i

# lsof
# lsof |wc -l


ps
===============

# ps -auxwf

high process id's which means it started late in the system where are processes running from - like running out tmp, root, dev

proc
===============
proc is your saviour alot of the times. Deletd processes after starting so it works and binary is gone so its hard to search
any hashing techniques or file changes is now gone from your system

look for deletd files or process files, high process ids, binary deleted starting, you can check what file is doing

# ls -al /proc/22551


strings
===============
Do not run strace on binary - strace is no good because it executes the binary. Can show game plan on binary

# strings /dev/binary


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

# find / -xdev -fstype xfs -nouser

All files and directories must have a valid group owner."
command: 

# find / -xdev -fstype xfs -nogroup

Find out all files that are not owned by any user:

# find / -nouser

Find out all files that are not owned by any group:

# find / -nogroup

For example in real life on busy clustered hosting server some time we remove 5-10 users and for security reasons you need to find out all files are not owned by any user or group then you can type command:

# find / -nogroup -nouse

