## Working with LVM

### Good reads

https://pingtool.org/online-resize-lvm-partitions-shrink-home-extend-root/
https://www.tecmint.com/extend-and-reduce-lvms-in-linux/
https://myshell.co.uk/blog/2012/08/how-to-extend-a-root-lvm-partition-online/


#### find UUID od disk/partition

	blkid

	/dev/mapper/VG_Home-lv_home: UUID="3d77b079-9587-455e-9ac4-8070dd7a3667" TYPE="ext4"

#### resize root partition online

	umount /home
	e2fsck -f /dev/mapper/vg_oracle-lv_home
	resize2fs /dev/mapper/vg_oracle-lv_home 20G
	lvreduce -L 20G /dev/mapper/vg_oracle-lv_home
	lvextend -l +100%FREE /dev/mapper/vg_oracle-lv_root
	resize2fs /dev/mapper/vg_oracle-lv_root
	mount /home

### create lvm part

Three steps to complete

1. fdisk - prepare disk
----------------

	fdisk /dev/sdb

this is creating the new disk getting it ready for lvm

	new partition = p
	1
	t
	change part to lvm = 8e
	print p to look at part
	press w to write
	restart server

2. lvm - create LVM partitions
-----------------
check disk with fdisk or lsblk

	pvcreate /dev/sdb
	pvs
	pvdisplay

3. vg_name can be anything that stands out to us

	vgcreate vg_name /dev/sdb
	vgs
	vgdisplay vg_name

lv_name can be anything too - make it understanding
	lvcreate --size +200G --name lv_name vg_name
	lvs
	lvdisplay

Examples:
vg_name =  vg_backupdrive
lv_name = lv_backups

It really can be anything. I always use the lettering vg and lv so I know Im looking at a volume group VG or logical volume lv

4. format partition

	mkfs.ext4 /dev/vg_name/lv_name

5. make a dir to mount the LVM to

	mkdir backups

	mount /dev/vg_name/lv_name /backups


6. make parition persistent

You might have to match the AWS format..maybe

	vim /etc/fstab

	/dev/vg_name/lv_name  /backups  ext4  defaults 0 0

You can run 

	mount -a 

if you choose instead of running mount /dev... /backups
Thsi will test if the fstab is working

7. reboot server and conquer


