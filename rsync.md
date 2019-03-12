## rsync

```bash
#!/bin/bash

rsync -chavzP --stats root@192.192.192.192:/home/rsync/ /home*

rsync -auHxv –numeric-ids –exclude=/etc/fstab –exclude=/etc/network/* –exclude=/proc/* –exclude=/tmp/* –exclude=/sys/* –exclude=/dev/* –exclude=/mnt/* –exclude=/boot/* –exclude=/root/* root@SRC-IP:/* /

rsync -arv --numeric-ids--exclude=/etc/fstab--exclude=/etc/network/*--exclude=/proc/* --exclude=/tmp/* --exclude=/sys/* --exclude=/dev/* --exclude=/mnt/* --exclude=/boot/* / example@192.192.192.192:/* 

#www server
#rsync -arv --progress --numeric-ids --exclude=/etc/fstab --exclude=/etc/network/* --exclude=/proc/* --exclude=/tmp/* --exclude=/sys/* --exclude=/dev/* --exclude=/mnt/* --exclude=/boot/* / root@@192.192.192.192:/

rsync -aruv --progress --numeric-ids --exclude=/etc/fstab --exclude=/etc/network/* --exclude=/proc/* --exclude=/tmp/* --exclude=/sys/* --exclude=/dev/* --exclude=/mnt/* --exclude=/boot/* / /
#use --dry-run
```