## Hardware Linux

#### mpstat

```bash
mpstat -P ALL 1
```

#### strace

```bash
strace
```

#### dmesg

```bash
dmesg |grep -i DMI
```

#### proc

Example

```bash
cat /proc/scsi
```

#### lscpu

#### lshw

--short

```bash
lshw -C system
```

#### hwinfo

```bash
hwinfo |egrep "vendor"
```

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

```bash
dmidecode -t
```

will show you the types available. You can use a number or the name to print only specific sections. Numbers start from 0(zero) as position 1.

or you can pass the name such as;

```bash
dmidecode -t bios
dmidecode -t system
dmidecode -t processor
dmidecode -t memory
```



