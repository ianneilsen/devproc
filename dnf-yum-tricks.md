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

	rpm -ql BitTorrent

Show me recently installed package

	rpm -qa --last

query information of a package

	rpm -qi vsftpd

verify a rpm

	rpm -Vp sqlbuddy-1.3.3-1.noarch.rpm

Import a rpm key

	rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6

List all imported keys

	rpm -qa gpg-pubkey*

#### Finding using DNF

	dnf info packageName

	dnf list installed

	dnf repolist

	dnf --enablerepo=*fedora install nano

	dnf remove httpd
	dnf  erase httpd

	remove all packages from a repo list
	dnf -v repolist
	dnf list installed | cat -n


#### Finding on Debian/Ubuntu systems

Debian / Ubuntu 	apt-cache show package 	Shows locally-cached info about a package.

	apt show package 	
	dpkg -s package 	Shows the current installed status of a package.

CentOS 	yum info package 	

	yum deplist package 	Lists dependencies for a package.

Fedora 	dnf info package 	

	dnf repoquery --requires package 	Lists dependencies for a package.

FreeBSD Packages 	

	pkg info package 	Shows info for an installed package.

Debian / Ubuntu 	sudo dpkg -i package.deb 	

	sudo apt-get install -y gdebi && sudo gdebi package.deb 	Installs and uses gdebi to install package.deb and retrieve any missing dependencies.

CentOS 	sudo yum install package.rpm 	
Fedora 	sudo dnf install package.rpm 	
FreeBSD Packages 	sudo pkg add package.txz 	
	sudo pkg add -f package.txz 	Installs package even if already installed.

Debian / Ubuntu 	sudo apt-get remove package 	
	sudo apt remove package 	
	sudo apt-get autoremove 	Removes unneeded packages.

CentOS 	sudo yum remove package 	

Fedora 	sudo dnf erase package 	

FreeBSD Packages 	sudo pkg delete package 	
	sudo pkg autoremove 	Removes unneeded packages.

FreeBSD Ports 	sudo pkg delete package 	
	cd /usr/ports/path_to_port && make deinstall 	De-installs an installed port.

Debian/Ubuntu
apt-get update 	apt update
apt-get dist-upgrade 	apt full-upgrade
apt-cache search string 	apt search string
apt-get install package 	apt install package
apt-get remove package 	apt remove package
apt-get purge package 	apt purge package

