## Hardware Linux

#### mpstat

mpstat -P ALL 1

#### strace

strace

#### dmesg

	dmesg |grep -i DMI

#### proc

Example

	cat /proc/scsi

#### lscpu

#### lshw

--short

lshw -C system

#### hwinfo

hwinfo |egrep "vendor"

#### lspci

#### lsscsi

#### lsusb

#### lsblk

#### inxi -Fx

#### df -h

#### fdisk

#### free

#### hdparm

#### dmidecode

#### smartctl -a


dmidecode -t
will show yout he types available. YOu can use a number or the name to print only specific sections. NUmbers start from 0(zero) as position 1.

or you can pass the name such as;
 
dmidecode -t bios

dmidecode -t system

dmidecode -t processor

dmidecode -t memory



