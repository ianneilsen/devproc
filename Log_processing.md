## Log greppping goodness

#### Good reads

https://github.com/awesome-lists/awesome-bash
https://www.the-art-of-web.com/system/logs/

### Using ossec to process logs

https://blog.sucuri.net/2016/03/server-security-anomaly-behaviour-with-ossec.html

#### Count Unique Visits

	$ cat access.log | awk '{ print $1 }' | sort | uniq -c | wc -l
# or today

	$ cat access.log | grep `date '+%e/%b/%G'` | awk '{ print $1 }' | sort | uniq -c | wc -l

# or this month

	$ cat access.log | grep `date '+%b/%G'` | awk '{ print $1 }' | sort | uniq -c | wc -l

#### Request IP Addresses

	$ cat access.log | awk '{ print $1 }' | sort | uniq -c | sort -rn | head -n 25
	$ cat access.log | awk '{ print $1 }' | sort | uniq -c | sort -rn | head -n 25 | awk '{ printf("%5d\t%-15s\t", $1, $2); system("geoiplookup " $2 " | cut -d \\: -f2 ") }'

#### 404 Request Responses

	$ cat access.log | awk '($9 ~ /404/)' | awk '{ print $7 }' | sort | uniq -c | sort -rn | head -n 25

#### Ranked by Response Codes

	$ cat access.log | awk '{ print $9 }' | sort | uniq -c | sort -rn

This simple command is very useful to quickly observe the total counts based on returned response code.

#### Most Popular URLS

	$ cat access.log | awk '{ print $7 }' | sort | uniq -c | sort -rn | head -n 25

A trivial replacement for some Google Analytics statistics, reporting how many hits the top 25 resources have tallied.

### Real-time IP-Page Requests

	$ tailf access.log | awk '{ printf("%-15s\t%s\t%s\t%s\n", $1, $6, $9, $7) }'
	$ tailf access.log | awk '{"geoiplookup " $1 " | cut -d \\: -f2 " | getline geo printf("%-15s\t%s\t%s\t%-20s\t%s\n", $1, $6, $9, geo, $7);}'

The final two commands are most likely my favorite as they provide me with real-time access information. These commands report on each IP address, request and response that have recently occurred on the server. Using tailf instead of a typical ‘tail -f’ has the benefit of not accessing the file when it is not growing

#### Awk

	awk '($8 ~ /404/)' access.log | awk '{print $8}' | sort | uniq -c | sort -rn

Similarly, for 502 (bad-gateway) we can run following command:

	awk '($9 ~ /502/)' access.log | awk '{print $7}' | sort | uniq -c | sort -r

#### Most requested URLs

	awk -F\" '{print $2}' access.log | awk '{print $2}' | sort | uniq -c | sort -r

#### Blank User Agents

A 'blank' user agent is typically an indication that the request is from an automated script or someone who really values their privacy. The following command will give you a list of ip addresses for those user agents so you can decide if any need to be blocked:

	awk -F\" '($6 ~ /^-?$/)' combined_log | awk '{print $1}' | sort | uniq

A further pipe through logresolve will give you the hostnames of those addresses.

#### processes

	ps -ef |awk '{ print $2 }' |tail -n +2 |while read pid; do echo "$pid $(lsof -p $pid |wc -l)"; done |sort -r -n -k 2 |while read pid count; do echo "$pid $count $(ps -o command= -p $pid)"; done

#### Kill a process running on port 8080

	$ lsof -i :8080 | awk '{l=$2} END {print l}' | xargs kill

#### Take values from a list (file) and search them on another file

	$ for ITEM in `cat values_to_search.txt`; do  (egrep $ITEM full_values_list.txt && echo $ITEM found) | grep "found" >> exit_FOUND.txt; done

#### Get executed script's current working directory

	$ CWD=$(cd "$(dirname "$0")" && pwd)

— by dhsrocha on Jan. 22, 2018, 4:55 p.m.
Explanation

Will return excuting script's current working directory, wherever Bash executes the script containing this line.

#### Blackhole ru zone

	$ echo "address=/ru/0.0.0.0" | sudo tee /etc/NetworkManager/dnsmasq.d/dnsmasq-ru-blackhole.conf && sudo systemctl restart network-manager

— by olshek_ on Nov. 14, 2017, 2:12 p.m.
Explanation

It creates dnsmasq-ru-blackhole.conf file with one line to route all domains of ru zone to 0.0.0.0.

You might use "address=/home.lab/127.0.0.1" to point allpossiblesubdomains.home.lab to your localhost or some other IP in a cloud.

#### Having turned up a number of 'Java' agents that we decided to block, we might want to investigate other request with similar user agents. For example, user agents starting with Java:

	awk -F\" '($6 ~ /^Java/)' combined_log | awk '{print $1}' | sort | uniq -c | sort -n

This returns a list of IP addresses similar to those above. The addresses we've already picked up will appear at the top, and you'll also see the less-active ones and have the option to investigate further.

As we mentioned at the start of this page, you're never going to be block all the 'bad' agents while letting in the good ones. There are simply too many possible variations. There are automated solutions for blocking IP addresses on a temporary or permanent basis based on behaviour, but that's a whole different ball-game.

#### A nicer way to block web sites is using ipsets and iptables. You have an iptables rule a bit like this

	ipset create crawlers hash:ip
	ipset add crawlers XX.173.68.90
	ipset add crawlers XX.184.192.199
	ipset add crawlers XXX.9.3.10
	ipset add crawlers XXX.231.187.166
	ipset add crawlers XXX.235.117.192
	iptables -A INPUT -p tcp --dport 80 --match set --set-name crawlers src -j REJECT

This has the advantage that it can be modified on the fly from the command line, without having to restart Apache.

#### return list of ips and addresses with number of hits

	awk '{print $1}' combined_log | sort | uniq -c | sort -n | tail -40 | awk '{print $2,$2,$1}' | logresolve | awk '{printf "%6d %s (%s)\n",$3,$1,$2}'

#### Display any tcp connections to apache

Sometimes apache will get stuck in an established state where you can't get a list of the connecting IP's from mod_status... not a good thing when you need to ban an abusive ip.

	for i in `ps aux | grep httpd | awk '{print $2}'`; do lsof -n -p $i | grep ESTABLISHED; done;

#### Top 10 requestors by IP address from Apache/NCSA Logs

	awk '{print $1}' /var/log/httpd/access_log | sort | uniq -c | sort -rnk1 | head -n 10

#### check for xss test regex

	grep -ahiP '[{}%<>]+' access_log* | grep -aiP "(?:<[\w/?]+)|(?:['\"\s/]*\bon[a-z]+?\s*=['\"\s]*)"

	grep for GET /%27%27
