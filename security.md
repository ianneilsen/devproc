## Security

https://www.cyberciti.biz/tips/linux-security.html
https://www.suse.com/documentation/sles11/book_hardening/data/sec_sec_prot_general_filepermissions.html
https://github.com/ethicalhack3r/DVWA

https://github.com/topics/defensive-security


### Good reads
https://cybercanon.paloaltonetworks.com/
https://www.devsecops.cc/
http://www.devsecops.org/
http://devsecops.github.io/
https://www.linux.com/
https://www.rootusers.com/category/security/
http://niiconsulting.com/checkmate/2017/06/a-detail-guide-on-oscp-preparation-from-newbie-to-oscp/

Red Team docs/ocsp
https://ired.team/


### Great Podcasts

* Purple Team
* ReplayAll
* DarkNet Diaries


### Good Tubes

https://www.youtube.com/watch?v=uIkxsBgkpj8


### Good blogs mail lists

https://www.schneier.com/

### Good githubs

https://github.com/future-architect/vuls
https://github.com/longld/peda
https://github.com/Neo23x0/
https://github.com/rfxn/
https://github.com/BlackArch/
https://github.com/forensic-architecture/

### Web based test solutions

https://securitytrails.com/

https://www.censys.io/certificates/help

https://www.shodan.io

https://www.secjuice.com/tag/unusual-journeys/

https://iphostinfo.com/cloudflare/

https://toolbar.netcraft.com/site_report?url=example.com

https://cloudpiercer.org/	


### Article posts for different work arounds

https://www.ericzhang.me/resolve-cloudflare-ip-leakage/


## Tools

https://securitytrails.com/

* etheral or tethereal
* driftnet - Chris Lightfoot
* etherpeg
* paketto
* mgsnarf
* scanrand
* fping

* gdb peda
* pwndbg

* setgsolv

hopper - static analysis

* Brute force
** hatch - python web login

* portswigger

* Empire
* shellz on github
* xte
* paramiko

* cobaltstrike

#### shell code

* shell-storm.org/shellcode/
* python pwn
* forkbombs

#### privelege escalations

https://github.com/FireFart/dirtycow/blob/master/dirty.c

#### Exploits

* Get exploits from multiple sources - https://github.com/BlackArch/sploitctl/blob/master/sploitctl.sh
* wso.php web shell - https://raw.githubusercontent.com/mIcHyAmRaNe/wso-webshell/master/wso.php

#### Post Exploitation
https://github.com/topics/post-exploitation

#### Logs

http://etutorials.org/Linux+systems/red+hat+linux+bible+fedora+enterprise+edition/Part+III+Administering+Red+Hat+Linux/Chapter+14+Computer+Security+Issues/Detecting+Intrusions+from+Log+Files/

* Flow logs
* scalp
* webforensics
* https://centos.pkgs.org/7/forensics-x86_64/LogAnalysisToolKit-1.7-1.el7.noarch.rpm.html
* https://github.com/jensvoid/lorg
* https://code.google.com/archive/p/apache-scalp/
* https://www.linode.com/docs/security/visualize-server-security-on-centos-7-with-an-elastic-stack-and-wazuh/


#### Forensics

* http://www.sleuthkit.org/
* http://www.porcupine.org/forensics/tct.html
* chkrootkit
* Autopsy
* eog
* https://github.com/cugu/awesome-forensics
* SAN run through on foresnics - chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/https://digital-forensics.sans.org/community/papers/gcfa/lessons-linux-compromise_209
* https://github.com/forensic-architecture/devops

#### DNS

* https://securitytrails.com
* https://toolbox.googleapps.com/apps/encode_decode/
* subdomain enumerator - https://github.com/aboul3la/Sublist3r
* intrigueio/intrigue-core

#### auth and sessions


#### xss

rsnake xss cheat sheet
xss research - ashar javed
mathias karlsson - pologlot payloads
github/flashbang - swf parameters xss

#### csrf

* burpy

#### sql

sqli pologlots - mathias karlsson
fuzzlists - seclists github by danielmessler
burp load seclists
blind is predominent sql injkection type
sqlmap - is king
-- parse burp log file using sqlmap and fuzz it
-- tamper scripts for blacklists - evade blacklists
sqlipy - burp plugin to instrument sqlmap

common params
- id, currency values, item numders, sorting params, json, xml values

mysql - pentestmonlkeys cheat sheet / reiners cheatsheet
posgtres - pentestmonkeys

#### file uploads

* liffy using seclists

#### idors

find user id's in web apps by moving through id's

#### transport mismatch

* ForceSSL - github


#### Network tools

* {Defense} -- DDOS analyzer - https://github.com/rfxn/fastnetmon

#### LISTS

https://github.com/danielmiessler/SecLists


#### Decoders

https://toolbox.googleapps.com/apps/encode_decode/
https://meyerweb.com/eric/tools/dencoder/
https://codebeautify.org/url-decode-string

#### Scanning

* Nessus
* OpenVAS
* OWASPZap
* Metasploit
* NMAP - yes nmap
* yara - signature base based which is good for sys admins and can be used on blueteaming - needs work and sig files from multiple sources
* Loki - opensource version of a very good scanner called THOR by nextron - https://github.com/Neo23x0/Loki

#### SSL/TLS 

https://testssl.sh/

#### Defensive mode - Blue team

* dns sink holes - block malware or CnC servers - know IP's
* look for known self-signed certs which malicious sites or servers use.

##### Defensive Analysis and forensics

* Carbonblack

#### Apache

* get mod_root

#### dir tools - web apps

RAFT Lists in seclists
SVN Digger in seclists
git digger

#### platform id'ing

Wapplyzer in chrome
BUiltwith in chrome
retire.js - burp or cli

#### Vul mapping OSINT - find bugs

xssed.com
reddit /r/xss
punkspider
xss.cx
xssposed.org
twitter


## Blueteam

### Yara rules

* https://github.com/rfxn/rules
* https://github.com/rfxn/Open-Source-YARA-rules

#### finger

https://linuxgeeksin.com/2017/04/16/finger-command-to-display-the-user-detail-in-centos-red-hat-fedora-ubuntu-scientific-linux-and-other-distributions/
https://www.thegeekstuff.com/2011/03/sar-examples/?utm_source=feedburner
https://techtalk.gfi.com/57-tips-admin/

### auditd

https://www.tecmint.com/create-reports-from-audit-logs-using-aureport-on-centos-rhel/
https://www.digitalocean.com/community/tutorials/how-to-use-the-linux-auditing-system-on-centos-7

#### Malware scanners

magento scanner - https://github.com/rfxn/magesecurityscanner
maldet - https://github.com/rfxn/linux-malware-detect

#### Detection tools EDR's

* CarbonBlack
* red canary
* fireye
* crowdstrike
* countercept
* endgame
* cylance 
* tanium
* Mitre alerts
* Sigma


#### SIEM

VirusTotal - https://www.virustotal.com/#/home/upload
https://cybercanon.paloaltonetworks.com/

#### OTX stuff

https://github.com/MISP/PyMISP
https://github.com/Neo23x0/Loki


#### Tripwire

#### ossec

https://www.vultr.com/docs/how-to-install-ossec-hids-on-a-centos-7-server

#### auditd

https://github.com/CISOfy/lynis
https://www.rfxn.com/

#### Log analysis

#### Icinga server monitoring

https://www.icinga.com/docs/icinga1/latest/en/verifyconfig.html

#### Courses

https://www.defensive-security.com/training-workshops
https://www.udemy.com/linux-security/

#### Look for hidden shell code
https://github.com/neohapsis/neopi