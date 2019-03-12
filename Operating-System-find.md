## Find what OS versions and details I am on

#### Most linux systems will run this

  $ cat /etc/*-release

```
Fedora release 26 (Twenty Six)
NAME=Fedora
VERSION="26 (Workstation Edition)"
ID=fedora
VERSION_ID=26
PRETTY_NAME="Fedora 26 (Workstation Edition)"
ANSI_COLOR="0;34"
CPE_NAME="cpe:/o:fedoraproject:fedora:26"
HOME_URL="https://fedoraproject.org/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=26
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=26
PRIVACY_POLICY_URL=https://fedoraproject.org/wiki/Legal:PrivacyPolicy
VARIANT="Workstation Edition"
VARIANT_ID=workstation
Fedora release 26 (Twenty Six)
Fedora release 26 (Twenty Six)
```

#### version from Debian/Ubuntu systems

  cat /etc/*_version

  cat /etc/*-release

#### hostnamectl where systemd installed

  $ hostnamectl

```
   Static hostname: local-ian
   Pretty hostname: local.ian
         Icon name: computer-laptop
           Chassis: laptop
        Machine ID: da558c7dacb146818bd4a514ca13b9ed
           Boot ID: cc09397abfde4509a7897df45afe1ce6
  Operating System: Fedora 26 (Workstation Edition)
       CPE OS Name: cpe:/o:fedoraproject:fedora:26
            Kernel: Linux 4.14.6-200.fc26.x86_64
      Architecture: x86-64
```

#### environments

  $ set
 
  $ env

#### proc

  cat /proc/cpuinfo

  cat /proc/meminfo

  cat /proc/disks

#### dmesg

  $ dmesg -H

#### pushd

  $ pushd /etc; pushd /var

#### apropos

  $ apropos search

#### iostat

  $ iostat
