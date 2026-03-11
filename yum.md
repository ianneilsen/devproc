## Working with yum

### Good reads
https://serverfault.com/questions/62026/how-to-know-from-which-yum-repository-a-package-has-been-installed
https://serverfault.com/questions/512788/how-to-install-32-bit-packages-on-a-64-bit-centos
https://www.centos.org/forums/viewtopic.php?t=43833
https://www.centos.org/forums/viewtopic.php?t=52551
https://access.redhat.com/solutions/265523
https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Deployment_Guide/sec-Removing.html
https://unix.stackexchange.com/questions/14589/listing-packages-in-yum-that-depend-on-another-installed-package
https://access.redhat.com/documentation/en-us/red_hat_subscription_management/1/html/rhsm/registering-cmd

#### List repos

```bash
	yum repolist all
```

#### yum list installed

```bash
	yum list installed

	yum list installed | grep lib123
```

#### Yum what provides this file

```bash
	yum whatprovides bind-libs-32:9.8.2-0
	
	yum whatprovides bind-libs

	repoquery -q --installed --whatrequires bind-devel

	rpm -q --whatrequires bind-devel
```

#### yum update commands

```bash	
	yum update --exclude bind-libs.i686
```

#### Show what an erase of a package will do

```bash
	rpm -e --test bind
```

#### You can list all repositories set up on your system by a yum repolist all. However, this does not show priority scores. Here's a one liner for that. If no number is defined, the default is the lowest priority (99).

```bash
	sed -n -e "/^\[/h; /priority *=/{ G; s/\n/ /; s/ity=/ity = /; p }" /etc/yum.repos.d/*.repo | sort -k3n 
```

### Show all packages available from a specific repository, e.g. RPMforge. This does not show the already installed packages from this repository.

```bash
	yum --disablerepo "*" --enablerepo "rpmforge" list available 
```

#### Getting rpm to display architecture

#### This one is a pretty simple tip, and very useful especially for people using x86_64 systems. Just one line in ~/.rpmmacros will save all sorts of trouble later

```bash
	echo "%_query_all_fmt %%{name}-%%{version}-%%{release}.%%{arch}" >> ~/.rpmmacros
```

#### Query packages not from CentOS

#### Want to query all those packages installed from 3rd party repositories, not CentOS?

```bash
	rpm -qa --qf '%{NAME} %{VENDOR}\n' | grep -v CentOS
```

### clean up yum

```bash
	yum clean all
```