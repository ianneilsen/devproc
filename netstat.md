## Netstat

#### Good Links

Show active connections

	netstat –tupn

#### Show listening ports

	netstat -lpn

#### check number of connections to this server

	netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n
 
	netstat -anp | grep :80 | grep TIME_WAIT | wc -l

#### Sort connected ips and count

	netstat -tn |awk '{print $5}' |cut -d: -f1 | sort | uniq -c |sort -nr


