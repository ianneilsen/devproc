## iptables

#### Good reads

https://crm.vpscheap.net/knowledgebase.php?action=displayarticle&id=29

#### show all rules/chains

	iptables -L -n --line-numbers

	iptables -L -n -v --line-numbers

	iptables -S

#### add rules

	iptables -A INPUT -p tcp -m tcp --dport 22 -m comment --comment "allow port 22" -j ACCEPT

	ipatbles -A INPUT -p tcp -m tcp --dport 22 -m comment --comment "not allow port 22" - j DROP

#### delete rule

delete rule by chain name and line number- is always the easiest method, generally.

	iptables _l -n --line-numbers
	iptables -D whitelist 19

### IPtables restrictions examples

-A INPUT -p tcp -m tcp --dport 22 -m state --state NEW -m recent --update --seconds 300 --hitcount 4 --name DEFAULT --rsource -j DROP

https://www.rackaid.com/blog/how-to-block-ssh-brute-force-attacks/

#### ssh stop brute force

/usr/sbin/iptables -I INPUT -p tcp --dport 22 -i eth0 -m state --state NEW -m recent --set
/usr/sbin/iptables -I INPUT -p tcp --dport 22 -i eth0 -m state --state NEW -m recent  --update --seconds 60 --hitcount 4 -j DROP

	-A INPUT -p tcp --dport 22 -i eth0 -m state --state NEW -m recent --set
	-A INPUT -p tcp --dport 22 -i eth0 -m state --state NEW -m recent  --update --seconds 60 --hitcount 3 -j DROP

#### prevent ddos

	iptables -A INPUT -p tcp --dport 80 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT

#### drop ips

	iptables -I global_drop -s 185.228.232.28 -m comment --comment "Malicious IP" -j DROP
	iptables -I global_drop -s 113.210.120.213 -m comment --comment "Malicious IP" -j DROP

#### Logging

You might also want to log all the dropped packets. These rules should be at the bottom.

First, create a new chain called LOGGING.

	iptables -N LOGGING

Next, make sure all the remaining incoming connections jump to the LOGGING chain as shown below.

	iptables -A INPUT -j LOGGING

Next, log these packets by specifying a custom “log-prefix”.

	iptables -A LOGGING -m limit --limit 2/min -j LOG --log-prefix "IPTables Packet Dropped: " --log-level 7

Finally, drop these packets.

iptables -A LOGGING -j DROP


