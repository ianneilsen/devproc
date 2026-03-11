## checking load on servers

#### Load checkin tools on linux

```bash
ps -eo pcpu,pid,user,args | sort -k 1 -r | head

mytop

mtop

iotop

iostat

iotop

atop

netstat

netatop

pstree = processes

sar

vmstat

uptime

free

swap - ps awwlx --sort=vsz

using `watch` in conjunction with one of the above

strace

tcpdump
```