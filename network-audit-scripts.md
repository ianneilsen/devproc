#### Network Auditing live

### Good reads

https://resources.infosecinstitute.com/category/enterprise/threat-hunting/iocs-and-artifacts/threat-hunting-for-ddos-activity-and-geographic-irregularities/#gref

## netstat

#### show all ips connected - if the number is high, like more than 10 or 20 then this is abnormal

  netstat -anp |grep 'tcp\|udp' | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n

##### show all connections to tcp ports

  $ netstat -at
  $ netstat -t

#### Good to show all connections and what they are connecting to

  $ netstat -natp

#### find listening programs

  $ netstat -ap | grep http

#### display in promiscuous mode

  $ netstat -ac 5 | grep tcp

#### good to see what is connecting

  $ ss -tp

## Advanced connection checks

#### Show ALL connections and which process is making connections

  $ ss -tp | grep -v Recv-Q | sed -e 's/.*users:(("//' -e 's/".*$//' | sort | uniq

  $ netstat -A example -p | grep '^tcp' | grep '/' | sed 's_.*/__' | sort | uniq

#### Show ESTABLISHED connections

  $ netstat -ntu | grep ESTAB | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr

#### List number of connections to IPs are making to tcp/udp

  $ netstat -anp |grep 'tcp\|udp'| awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n

  $ netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n

#### show number of connections by IP

  $ netstat -atun | awk '{print $5}' | cut -d: -f1 | sed -e '/^$/d' |sort | uniq -c | sort -n

#### show connections by state

  $ netstat -nat | awk '{print $6}' | sort | uniq -c | sort -n

Processes/Files/Users
-------------------------

#### LIST ALL process/sockets and examples

#### Using lsof

  $ lsof -i
  $ lsof -i -a
  $ lsof -i -a -c ssh

#### find malicious processes in linux

  $ lsof -Pni
  $ lsof -RPni <:portnumber>
  $ lsof -Pnp <pid>

  $ lsof -i tcp:80 -P -R
  $ lsof -p PIDNumber
  $ lsof -i @hostname
  $ lsof +d /var/log/apache

  netstat /ano

#### Using netstat

  $ netstat -an
  $ netstat -tulpn
  $ netstat -tup

  netstat -plunt or plunta 

#### using iftop

  $ iftop -p

#### Using ss

Processes
--------------------

#### Process audit tricks - GOOD

  $ lsof -Pwln
  $ ps axfo pid,ppid,sess,uid,cmd --sort=pid

#### Show processes run by a user

  top -c -u terdon

Files
---------------

#### Find open used temp deleted files

  $ lsof -n | grep '(deleted)'

#### Using a file, find which process it is

  $ fuser filename

#### More complicated use of PROC to find which process is using the FILE

  $ find /proc -regex '\/proc\/[0-9]+\/fd\/.*' -type l -lname "*$1*" -printf "%p -> %l\n" 2> /dev/null

#### find what files a process has open

  ls -l /proc/process-pid/*
  losf -p process-pid

OUTGOING connections
--------------------------

  netstat -nputw
  ss -tpa

  watch netstat -nputw
  watch ss -tpa

links https://www.binarytides.com/linux-ss-command/

#### watch connections using lsof and watch. You can use WATCH with netstat also

  watch -d -n1 lsof -i

##### watches sockets

  ss -nap

  ss -tlp

Stopping connections
----------------------------

#### IPtables rules to help stop high connection counts -- 2 new iptables rules

  -I INPUT -p tcp -i eth0 -m state —state NEW —dport 80 -m recent —set
  -I INPUT -p tcp -i eth0 -m state —state NEW —dport 80 -m recent —update —seconds 60 —hitcount 20 -j DROP
  -I INPUT -p tcp -i eth0 -m state —state NEW —dport 443 -m recent —set
  -I INPUT -p tcp -i eth0 -m state —state NEW —dport 443 -m recent —update —seconds 60 —hitcount 20 -j DROP

  # syn check
  #-N syn_flood
  #-A INPUT -p tcp --syn -j syn_flood
  #-A syn_flood -m limit --limit 1/s --limit-burst 3 -j RETURN
  #-A syn_flood -j DROP

## Limit connections per second to eth interface

  -I INPUT -p tcp --dport 80 -i eth0 -m state --state NEW -m recent --name ddos_protection --set
  -I INPUT -p tcp --dport 80 -i eth0 -m state --state NEW -m recent --name ddos_protection --update --seconds 15 --hitcount 10 -j DROP

## lIMIT CONNECTIONS TO PORT 80 FROM A SINGLE IP USING A MASK

  -A INPUT -p tcp --dport 80 -m connlimit --connlimit-above 50 --connlimit-mask 20 -j DROP
  -A INPUT -p tcp --syn --dport 80 -m connlimit --connlimit-above 100 -j DROP

Syn details
---------------------

#### check syn flood attacks

  netstat | grep 'SYN_RECV' | wc -l
  netstat | grep 'SYN_RECV' | awk {'print $6'} | cut -f 1 -d ":" | sort | uniq -c | sort -k1,1rn | head -10

##### Show SYN  - must be root to get all back

  netstat -n -p | grep SYN_REC | awk '{print $5}' | awk -F: '{print $1}'

Links
---------

https://www.predictiveanalyticstoday.com/list-security-event-management-log-analysis-software/
https://blog.profitbricks.com/top-47-log-management-tools/
https://www.blackmoreops.com/2014/09/25/find-number-of-unique-ips-active-connections-to-web-server/
http://www.codedwell.com/post/62/unix-shell-commands-to-detect-ddos-attack
http://www.uberobert.com/nagios-check-for-tcp-syn-flooding-attacks/
http://www.riorey.com/types-of-ddos-attacks/
https://security.stackexchange.com/questions/7443/how-do-you-know-your-server-has-been-compromised

### count ip s in access.log

  cat access.log | awk '{print $1}' | sort -n | uniq -c | sort -nr | head -20

  cat access.* | awk '{ print $1 } ' | sort | uniq -c | sed -r 's/^[ \t]*([0-9]+) (.*)$/\1 --- \2/' | sort -rn

  cat access.log |grep -v -w 200 | grep -v -w 403 | grep -v -e '.jpg'|grep -v -i bot | awk '{print $1}' | sort -n | uniq -c | sed -r 's/^[ \t]*([0-9]+) (.*)$/\1 --- \2/' | sort -nr | head -200

  cat access.* | awk '{ print $1 }' | sort | awk '{print $1 " " $2;}' | sort -n

  cat $LOG_FILE | awk '{print $1}' | sort | uniq -c | sort -nr | head -n 20


```bash
#!/bin/bash
LOG_FILE=/var/www/vhosts/DOMAIN.co.uk/statistics/logs/access_log
OUT_FILE=/tmp/spider_analysis

#This generates a file with the top 20 IP addresses by number of requests
cat $LOG_FILE | awk '{print $1}' | sort | uniq -c | sort -nr | head -n 20 > $OUT_FILE

echo "Top 20 IP addresses by number of request"
cat $OUT_FILE

#allow for loop to split on new line
IFS_BAK=$IFS
IFS="
"

for i in `cat $OUT_FILE`
do
    
COUNT=`echo $i | awk '{print $1}'`
    IP_ADD=`echo $i | awk '{print $2}'`
    echo ""
    echo "---------------------------------"
    echo ""
    echo "$IP_ADD has made $COUNT requests"
    echo "Whois Information"
    whois $IP_ADD 
    #lynx -dump http://who.cc/$IP_ADD # whois was blocked on the server i was using for some reason, use lynx as a work around
    echo ""
    echo "---------------------------------"
    echo ""
done

# set that back
IFS=$IFS_BAK
IFS_BAK=
```


  awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -nr

  grep 'text' /path/to/access.log | cut -d' ' -f1 | sort | uniq -c | sort -r
