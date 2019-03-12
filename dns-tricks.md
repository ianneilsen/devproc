dns tricks
==========

#### Good links

https://stackoverflow.com/questions/38021/how-do-i-find-the-authoritative-name-server-for-a-domain-name


Global DNS propogation checker
https://www.whatsmydns.net/

use open dns
https://www.opendns.com/

Using nslookup to find domain information
https://www.tecmint.com/8-linux-nslookup-commands-to-troubleshoot-dns-domain-name-server/


world ip ranges
=-------------\

nirsoft


====dig====


dig domainname.com

#### reversedns

host 123.123.123.123

dig -x 123.123.123.123

dig +noall +answer -x 123.123.123.123


#### traceroute

traceroute -T -p 80 123.123.123.123

#### how to check dkim records
https://scottlinux.com/2012/10/27/how-to-fetch-dkim-records-from-dns/

dig -t ns <domain name>

host -t ns stackoverflow.com
dig SOA +trace stackoverflow.com
whois stackoverflow.com
nslookup
> set querytype=soa
> stackoverflow.com

nslookup -type=soa stackoverflow.com
dig +short NS stackoverflow.com
dig +short  SOA stackoverflow.com | cut -d' ' -f1


#### Check a list of names for dns info

for i in `cat bulkregister.txt`; do printf "$i\n" ; dig NS $i +short;printf "\n";done




