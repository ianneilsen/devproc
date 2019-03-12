## All things passwords

### reset fedora passwords

New school
https://fedoramagazine.org/reset-root-password-fedora/

Old school


    boot with init=/bin/bash (editing the kernel line in grub)
    after booting: mount -o remount,rw /
    passwd root
    enter the new password twice
    touch /.autorelabel
    reboot with /sbin/reboot -f

The last line (creating the .autorelabel file at the root) force a selinux relabelling of the whole filesystem, which is corrupted since we modified /etc/shadow without any selinux context (because of booting with init=/bin/bash).

Bugzilla: https://bugzilla.redhat.com/show_bug.cgi?id=1084400

Updated Fedora wiki with the selinux fix: https://fedoraproject.org/w/index.php?title=How_to_reset_a_root_password#Changing_root_password


