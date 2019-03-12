Elastic stack commands
========================

Tools/scripts
====================


ELASTIC guests info
----------------


       elastic guests list | elastic guests info | grep email | cut -d " " -f2
       elastic  guests
       elastic  guests list
       elastic  guests info
       elastic  guests info ee06dbc2-39d7-4c20-9fc7-86d6930bab23
       elastic  guests ee06dbc2-39d7-4c20-9fc7-86d6930bab23 info

THE FOLLOWING TELLS ME ABOUT A VM - VM BEING B243....

       elastic guests b243bae6-46b2-4aa7-850f-d5aecfa478b1 info

```bash
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
```

Elastic ATOP
----------

       atop

Elastic PS
-----------

       ps aux --sort=-pcpu,+pmem |head -10


Example output which has been cleaned up for easier reading
--------------------------------------------------

```bash
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
```

## Elastic commands

```bash
elastic
Usage: elastic [help]
       elastic containers [ARG]...
       elastic drives [ARG]...
       elastic guests [ARG]...
       elastic host [ARG]...
       elastic pools [ARG]...
       elastic service [ARG]...
       elastic volumes [ARG]...
```

```bash
elastic service  
Usage: elastic service restart server
       elastic service restart sshd
       elastic service restart iscsid
       elastic service restart rsyslogd
       elastic service restart dnsmasq
       elastic service restart firewall
```

```bash
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
```


var/log is a good place to look for issues.
