## ipmi tools or linux and iDRAC access

sudo add-apt-repository 'deb http://ftp.de.debian.org/debian jessie main '

add-apt-repository 'deb http://archive.debian.org/debian/dists/ squeeze main'

racadm config -g cfgUserAdmin -o cfgUserAdminPassword -i 2 REDACTED

# ipmitool -I bmc lan set 1 ipaddr 192.0.2.37
# ipmitool -I bmc lan set 1 netmask 255.255.255.0
# ipmitool -I bmc lan set 1 defgw ipaddr 192.0.2.1


ipmitool lan set 1 ipaddr 192.0.2.211
ipmitool lan set 1 netmask 255.255.255.0
ipmitool lan set 1 defgw ipaddr 192.0.2.1
ipmitool lan set 1 auth ADMIN MD2 MD5 PASSWORD
ipmitool lan set 1 access on


ipmitool -H 192.0.2.17 -U example lan print 1
ipmitool -H 206.191.128.140 -U example lan print 1


ipmitool user list 2
ipmitool user summary 2
ipmitool bmc info
ipmitool lan print 1
ipmitool lan print 1
ipmitool channel getaccess 2 2
ipmitool channel getaccess 2 3

ipmitool user set name 2 admin
ipmitool user set password 2
ipmitool channel setaccess 1 3 link=on ipmi=on callin=on privilege=4
ipmitool user enable 2

ipmitool user set name 3 example
   32  ipmitool user set password 3 REDACTED
   33  ipmitool user enable 3
   34  ipmitool channel setaccess 1 3 privilege=4
   35  ipmitool channel setaccess 1 3 link=on
   36  ipmitool channel setaccess 1 3 ipmi=on
   37  ipmitool lan print 1
   38  ipmitool user summary 3

for i in `seq 1 14`; do ipmitool channel info $i ; done

