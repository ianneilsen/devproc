## pci auditing tricks

### Good Links

https://static.open-scap.org/ssg-guides/ssg-centos7-guide-pci-dss.html#xccdf_org.ssgproject.content_group_accounts

https://people.redhat.com/swells/scap-security-guide/tables/table-rhel7-pcidssrefs.html

https://linux-audit.com/linux-systems-guide-to-achieve-pci-dss-compliance-and-certification/

### Rule by rule guide to hardening Linux for PCI

https://people.redhat.com/swells/scap-security-guide/tables/table-rhel7-pcidssrefs.html

### check for installed packges which have ssl/tls used

	for I in $(find /usr/sbin -type f -print); do ldd ${I} | egrep -q "(ssl|tls)"; if [ $? -eq 0 ]; then echo ${I}; fi; done
