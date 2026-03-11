## Forensics for Linux

Pen testing is mostly fairly easy with todays tools, but finding and understanding intrusions should'nt be hard.

Below is a list of commands you can intially run on linux boxes to uncover potential compromises.

As a sysadmin or blue team'er you should know your systems back to front. What should be there and what shouldnt. 

Docuemntation is king, using something like Ansible, puppet, chef or salt to ensure you base systems as are they should be.

Protect your backups at all cost.

#### Im compromised now what

I suggest you take a copy of the drives in your system so you can run forensic tools against the clone disks

#### Check memory

The big 5
===========

### Processes

```bash
top
htop
ps -auxwf
netstat -nalp
netstat -plant
ss -a -e -i
lsof
```

del binaries still running

```bash
ls -alR /proc/*/exe 2> /dev/null | grep deleted
```

Process command

```bash
strings /proc/PID/comm
strings /proc/PID/cmdline
```

Real path

```bash
ls -al /proc/PID/exe
```

Process enviro

```bash
strings /proc/PID/environ
```

Process working dir

```bash
ls -alR /proc/*/cwd
```

Process in tmp,dev dirs

```bash
ls -alR /proc/*/cwd 2> /dev/null | grep tmp
ls -alR /proc/*/cwd 2> /dev/null | grep dev
```

### Directories

dirs with spaces in names

```bash
ls -lap
```

Hidden dirs

```bash
find / -type d -name ".*"
```

### Files

Find executables

```bash
find / -type f -exec file -p '{}' \; | grep ELF
```

Immutable files & dirs

```bash
lsattr / -R 2> /dev/null | grep "\----i"
```

Find suid/sgid files

```bash
find / -type f \(-perm -04000 -o -perm -02000 \) -exec ls -lg {} \;
```

Persistent areas

```bash
/etc/rc.local
/etc/initd
/etc/rc*.d
/etc/modules
/etc/cron*
/var/spool/cron
```

### Users

Hist files linked to /dev/null

```bash
ls -alR / 2>/dev/null |grep .*history | grep null
```

UID 0

```bash
grep ":0:" /etc/passwed
```

sudoers

```bash
cat /etc/sudoers
cat /etc/group
```

Cron

```bash
cat /var/spool/cron/*
crontab -l
atq
systemctl list-timers --all
```

### Logs

```bash
grep [[:cntrl]] /var/log/*.log
```

