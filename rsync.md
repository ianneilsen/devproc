## rsync

### basic
```bash
rsync -chavzP --stats root@192.192.192.192:/home/rsync/ /home*

rsync -auHxv –numeric-ids –exclude=/etc/fstab –exclude=/etc/network/* –exclude=/proc/* –exclude=/tmp/* –exclude=/sys/* –exclude=/dev/* –exclude=/mnt/* –exclude=/boot/* –exclude=/root/* root@SRC-IP:/* /

rsync -arv --numeric-ids--exclude=/etc/fstab--exclude=/etc/network/*--exclude=/proc/* --exclude=/tmp/* --exclude=/sys/* --exclude=/dev/* --exclude=/mnt/* --exclude=/boot/* / <username>@<remote_ip>:/*
```

### from www server

```bash
rsync -arv --progress --numeric-ids --exclude=/etc/fstab --exclude=/etc/network/* --exclude=/proc/* --exclude=/tmp/* --exclude=/sys/* --exclude=/dev/* --exclude=/mnt/* --exclude=/boot/* / root@@192.192.192.192:/
```

### dry run

```bash
rsync -aruv --progress --numeric-ids --exclude=/etc/fstab --exclude=/etc/network/* --exclude=/proc/* --exclude=/tmp/* --exclude=/sys/* --exclude=/dev/* --exclude=/mnt/* --exclude=/boot/* / /

```