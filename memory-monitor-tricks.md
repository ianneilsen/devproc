##Monitoring Memory on nix servers

#### Using ps to find memory hogs

	ps -eo pmem,pcpu,vsize,pid,cmd | sort -k 1 -nr | head -5

Really good pss mmeory check

	ps aux | awk '{print $4"t: " "PID:"$3 $11}' | sort | uniq -c | awk '{print $2" "$1" "$3}' | sort -nr
	or
	ps aux | awk '{print "Mem:"$4"t " "PID:"$2 $11}' | sort | uniq -c | awk '{print $2" "$1" "$3}' | sort -nr | head -30


Example output
```bash
3.7t/usr/lib64/firefox/firefox 1 
3.2t/usr/lib64/firefox/firefox 1 
3.0t/usr/lib64/firefox/firefox 1
```

Example

	ps -eo pmem,pcpu,vsize,pid,cmd | sort -k 1 -nr | head -10

#### use htop
Sort by memory and expand sort to see process. Almost the same output as the ps command above

	htop

#### show all processes sorted by memory use in MBs

	ps aux  | awk '{print $6/1024 " MB\t\t" $11}'  | sort -n

```bash
115.809 MB		/usr/bin/python2
116.145 MB		/usr/bin/gnome-shell
128.473 MB		/opt/google/chrome/chrome
143.262 MB		/opt/google/chrome/chrome
```

#### show all process sorted by cpu, pid, userm args top 10

	ps -eo pcpu,pid,user,args | sort -k 1 -r | head -10
    
```bash
%CPU   PID USER     COMMAND
 0.0     9 root     [rcu_sched]
 0.0     8 root     [rcu_bh]
 0.0   883 root     /sbin/dhclient -d -q -sf /usr/libexec/nm-dhcp-helper -pf /var/run/dhclient-eth0.pid -lf /var/lib/NetworkManager/dhclient-d353f01e-a2bc-46ef-88bf-03682e9036eb-eth0.lease -cf /var/lib/NetworkManager/dhclient-eth0.conf eth0
 0.0     7 root     [migration/0]
 0.0   759 root     /usr/sbin/NetworkManager --no-daemon
 0.0   745 chrony   /usr/sbin/chronyd
 0.0   742 root     /bin/bash /usr/sbin/ksmtuned
 0.0   741 root     /usr/sbin/spice-vdagentd
 0.0   720 root     /usr/sbin/alsactl -s -n 19 -c -E ALSA_CONFIG_PATH=/etc/alsa/alsactl.conf --initfile=/lib/alsa/init/00main rdaemon
```