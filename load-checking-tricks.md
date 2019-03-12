## Load testing on linux

	ps -eo pcpu,pid,user,args | sort -k 1 -r | head -10

	ps aux | tail -n +2 | awk {'print $1'} | sort | uniq -c | sort -rn

#### Find files which have changed.

Network

https://linuxaria.com/howto/how-to-verify-ddos-attack-with-netstat-command-on-linux-terminal

#### Processes check using ps

Find all duplicate processes using ps and count them

	ps aux | sort --key=11 | uniq -c -d --skip-fields=10 | sort -nr --key=1,1




