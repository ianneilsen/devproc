## dnf yum tricks


#### Good reads
https://fedoraproject.org/wiki/Yum_to_DNF_Cheatsheet 
https://unix.stackexchange.com/questions/157060/how-to-merge-config-files-interactively-after-yum-update
https://www.digitalocean.com/community/tutorials/package-management-basics-apt-yum-dnf-pkg
https://dnf.readthedocs.io/en/latest/command_ref.html


#### Find which package a lib belongs to
https://linux-audit.com/determine-file-and-related-package/
https://linux-audit.com/determine-file-and-related-package/

List all files of a package

```bash
rpm -ql BitTorrent
```

Show me recently installed package

```bash
rpm -qa --last
```

query information of a package

```bash
rpm -qi vsftpd
```

verify a rpm

```bash
rpm -Vp sqlbuddy-1.3.3-1.noarch.rpm
```

Import a rpm key

```bash
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6
```

List all imported keys

```bash
rpm -qa gpg-pubkey*
```

#### Finding using DNF

```bash
dnf info packageName
dnf list installed
dnf repolist
dnf --enablerepo=*fedora install nano
dnf remove httpd
dnf erase httpd
```

remove all packages from a repo list

```bash
dnf -v repolist
dnf list installed | cat -n
```

#### Finding on Debian/Ubuntu systems

Debian / Ubuntu - Shows locally-cached info about a package.

```bash
apt-cache show package
apt show package
dpkg -s package
```

CentOS

```bash
yum info package
yum deplist package
```

Fedora

```bash
dnf info package
dnf repoquery --requires package
```

FreeBSD Packages - Shows info for an installed package.

```bash
pkg info package
```

Debian / Ubuntu

```bash
sudo dpkg -i package.deb
sudo apt-get install -y gdebi && sudo gdebi package.deb
```

CentOS / Fedora / FreeBSD

```bash
sudo yum install package.rpm
sudo dnf install package.rpm
sudo pkg add package.txz
sudo pkg add -f package.txz
```

Debian / Ubuntu - Remove packages

```bash
sudo apt-get remove package
sudo apt remove package
sudo apt-get autoremove
```

CentOS / Fedora / FreeBSD - Remove packages

```bash
sudo yum remove package
sudo dnf erase package
sudo pkg delete package
sudo pkg autoremove
cd /usr/ports/path_to_port && make deinstall
```

Debian/Ubuntu

```bash
apt-get update
apt-get dist-upgrade
apt-cache search string
apt-get install package
apt-get remove package
apt-get purge package
```

