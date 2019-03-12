Elastic stack commands
========================


Tools/scripts
====================

ELASTIC TOOL - ON EACH SERVER
----------------

elastic guests list | elastic guests info | grep email | cut -d " " -f2
elastic  guests
elastic  guests list
elastic  guests info
elastic  guests info ee06dbc2-39d7-4c20-9fc7-86d6930bab23
elastic  guests ee06dbc2-39d7-4c20-9fc7-86d6930bab23 info

THE FOLLOWING TELLS ME ABOUT A VM - VM BEING B243....

elastic guests b243bae6-46b2-4aa7-850f-d5aecfa478b1 info

Usage: elastic guests create
       elastic guests info
       elastic guests list
       elastic guests tidy [force]
       elastic guests GUEST continue
       elastic guests GUEST create [incoming [block]]
       elastic guests GUEST destroy
       elastic guests GUEST info [raw]
       elastic guests GUEST kill
       elastic guests GUEST migrate HOST PORT [block] [destroy]
       elastic guests GUEST migrate cancel
       elastic guests GUEST migrate drive
       elastic guests GUEST pause
       elastic guests GUEST reset
       elastic guests GUEST revive
       elastic guests GUEST set
       elastic guests GUEST shutdown
       elastic guests GUEST stats


ATOP
----------
atop

PS
-----------

ps aux --sort=-pcpu,+pmem |head -10

look for /var/lib/guests/d53fe2a2-65c6-4ee9-891d-287b6d99c80c/qemu.pid 

Example output which has been cleaned up for easier reading
--------------------------------------------------
USER 65546    
PID 11922  
CPU% 141  
MEM% 3.2 
VSZ 3002504 
RSS 2167116 ?     
TTY S<l   
START 2018 523182:06
COMMAND (WHICH IS BELOW) 
qemu-system-x86-fallback 
-enable-kvm 
-runas 65546:65546 
-pidfile /var/lib/guests/eaa5e731-a23b-48ca-855f-950bcf83d3da/qemu.pid 
-nodefaults 
-m 2048 
-smp sockets=1,cores=4 
-cpu host 
-vga cirrus 
-usbdevice tablet 
-uuid eaa5e731-a23b-48ca-855f-950bcf83d3da 
-smbios file=/var/lib/guests/eaa5e731-a23b-48ca-855f-950bcf83d3da/smbios.bin 
-boot order=cd,menu=off 
-drive if=none,id=ide.0.0,format=raw,cache=writeback,file=/dev/mapper/guest:eaa5e731-a23b-48ca-855f-950bcf83d3da:ide:0:0 
-device ide-drive,bus=ide.0,unit=0,bootindex=1,drive=ide.0.0 
-device e1000,id=nic.0,mac=56:0b:cf:83:d3:da,netdev=vlan.0 
-netdev tap,id=vlan.0,ifname=vnet10.0, script=no,downscript=no 
-vnc :221,password,websocket=6122 
-monitor unix:/var/lib/guests/eaa5e731-a23b-48ca-855f-950bcf83d3da/monitor,server,nowait 
-name east5 new

HOSTS - physical HOSTS
==========

NORMAL DEBIAN HOSTS
0005a60e-883a-4fdc-ba17-50426ac51839

0006ae31-3311-454b-b4d4-54b2ffbb0bc6

0007aaaa-b688-4701-ab55-a541825f2dca

0008d56d-7fd5-4336-ad37-1e3f37e33034

0009afc4-1242-468c-a567-174230862bbc

0010fcca-1ff0-4591-98d1-ceb3f98f4e9d

0011d5a2-7ede-42d7-a80e-987895348d37

DEBAIN HOST WHICH ACTS PURELY AS A CONTAINER SERVER
1001cccc-143a-4e3d-a350-3c6c9f5f347d


elastic
Usage: elastic [help]
       elastic containers [ARG]...
       elastic drives [ARG]...
       elastic guests [ARG]...
       elastic host [ARG]...
       elastic pools [ARG]...
       elastic service [ARG]...
       elastic volumes [ARG]...

6.oh:~ # elastic service  
Usage: elastic service restart server
       elastic service restart sshd
       elastic service restart iscsid
       elastic service restart rsyslogd
       elastic service restart dnsmasq
       elastic service restart firewall


elastic-diskaudit       
elastic-iotop           
elastic-nettop          
elastic-sshd            
elastic-cgroups         
elastic-floodwatch      
elastic-monitoring      
elastic-pool            
elastic-syslog-handler  
elastic-coredump        
elastic-iostats         
elastic-netstats        
elastic-revive          
elastic-volume 



var/log is a good place to look for issues.
