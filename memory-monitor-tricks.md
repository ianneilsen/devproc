##Monitoring Memory on nix servers

#### Using ps to find memory hogs

	ps -eo pmem,pcpu,vsize,pid,cmd | sort -k 1 -nr | head -5

Example

```bash
# ps -eo pmem,pcpu,vsize,pid,cmd | sort -k 1 -nr | head -10
12.6  2.6 794528 11444 sidekiq 5.0.4 gitlab-rails [0 of 25 busy]
12.5  0.7 1031004 11593 unicorn worker[0] -D -E production -c /var/opt/gitlab/gitlab-rails/etc/unicorn.rb /opt/gitlab/embedded/service/gitlab-rails/config.ru
12.3  0.7 902212 12356 unicorn worker[1] -D -E production -c /var/opt/gitlab/gitlab-rails/etc/unicorn.rb /opt/gitlab/embedded/service/gitlab-rails/config.ru
12.3  0.7 902212 12326 unicorn worker[2] -D -E production -c /var/opt/gitlab/gitlab-rails/etc/unicorn.rb /opt/gitlab/embedded/service/gitlab-rails/config.ru
 9.0  1.6 593852 11534 unicorn master -D -E production -c /var/opt/gitlab/gitlab-rails/etc/unicorn.rb /opt/gitlab/embedded/service/gitlab-rails/config.ru
 3.7  0.5 1390580 11372 bin/gitaly-ruby 11321 /tmp/gitaly-ruby772494817/socket
 1.4  0.4 509124 11422 /opt/gitlab/embedded/bin/prometheus -web.listen-address=localhost:9090 -storage.local.path=/var/opt/gitlab/prometheus/data -storage.local.chunk-encoding-version=2 -storage.local.target-heap-size=105711288 -config.file=/var/opt/gitlab/prometheus/prometheus.yml
 1.2  0.0 1057652 11413 /opt/gitlab/embedded/bin/postgres -D /var/opt/gitlab/postgresql/data
 0.7  0.4 312136 11360 /opt/gitlab/embedded/bin/ruby /opt/gitlab/embedded/bin/gitlab-mon web -c /var/opt/gitlab/gitlab-monitor/gitlab-monitor.yml
 0.6  0.0 1057756 11415 postgres: checkpointer process ```
```

#### use htop

	htop

sort by memory and expand sort to see process. Almost the same output as
the ps command above

#### show all processes sorted by memory use in MBs

	ps aux  | awk '{print $6/1024 " MB\t\t" $11}'  | sort -n

```bash
115.809 MB		/usr/bin/python2
116.145 MB		/usr/bin/gnome-shell
128.473 MB		/opt/google/chrome/chrome
143.262 MB		/opt/google/chrome/chrome
150.941 MB		/opt/google/chrome/chrome
153.555 MB		/opt/google/chrome/chrome
158.125 MB		/usr/libexec/packagekitd
170.312 MB		/opt/google/chrome/chrome
248.152 MB		/proc/self/exe
351.621 MB		/opt/google/chrome/chrome
357.777 MB		/opt/google/chrome/chrome
417.988 MB		/opt/google/chrome/chrome
469.836 MB		/usr/bin/gnome-shell
477.211 MB		/usr/libexec/Xorg
483.316 MB		/usr/lib64/thunderbird/thunderbird
496.664 MB		/opt/google/chrome/chrome
649.367 MB		/usr/lib64/firefox/firefox
940.582 MB		/mywork/setups/pycharm-community-2017.2.2/jre64/bin/java
1014.21 MB		/usr/lib64/firefox/firefox
1180.59 MB		/opt/google/chrome/chrome
2058.93 MB		/usr/bin/qemu-system-x86_64

```

#### show all process sorted by cpu, pid, userm args top 10

	ps -eo pcpu,pid,user,args | sort -k 1 -r | head -10
    
```bash
%CPU   PID USER     COMMAND
 0.0     9 root     [rcu_sched]
 0.0     8 root     [rcu_bh]
 0.0   883 root     /sbin/dhclient -d -q -sf /usr/libexec/nm-dhcp-helper -pf /var/run/dhclient-eth0.pid -lf /var/lib/NetworkManager/dhclient-d353f01e-a2bc-46ef-88bf-03682e9036eb-eth0.lease -cf /var/lib/NetworkManager/dhclient-eth0.conf eth0
 0.0     7 root     [migration/0]
 0.0   759 root     /usr/sbin/NetworkManager --no-daemon
 0.0   745 chrony   /usr/sbin/chronyd
 0.0   742 root     /bin/bash /usr/sbin/ksmtuned
 0.0   741 root     /usr/sbin/spice-vdagentd
 0.0   720 root     /usr/sbin/alsactl -s -n 19 -c -E ALSA_CONFIG_PATH=/etc/alsa/alsactl.conf --initfile=/lib/alsa/init/00main rdaemon
 0.0   719 polkitd  /usr/lib/polkit-1/polkitd --no-debug
 0.0   717 root     /sbin/rngd -f
 0.0   712 root     /usr/bin/abrt-watch-log -F Backtrace /var/log/Xorg.0.log -- /usr/bin/abrt-dump-xorg -xD
 0.0     6 root     [kworker/u4:0]
 0.0   689 avahi    avahi-daemon: chroot helper
 0.0   688 root     /usr/sbin/gssproxy -D
 0.0   677 dbus     /bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation
 0.0   672 root     /usr/bin/abrt-watch-log -F BUG: WARNING: at WARNING: CPU: INFO: possible recursive locking detected ernel BUG at list_del corruption list_add corruption do_IRQ: stack overflow: ear stack overflow (cur: eneral protection fault nable to handle kernel ouble fault: RTNL: assertion failed eek! page_mapcount(page) went negative! adness at NETDEV WATCHDOG ysctl table check failed : nobody cared IRQ handler type mismatch Machine Check Exception: Machine check events logged divide error: bounds: coprocessor segment overrun: invalid TSS: segment not present: invalid opcode: alignment check: stack segment: fpu exception: simd exception: iret exception: /var/log/messages -- /usr/bin/abrt-dump-oops -xtD
 0.0   671 root     /usr/sbin/abrtd -d -s
 0.0   670 root     /usr/bin/qemu-ga --method=virtio-serial --path=/dev/virtio-ports/org.qemu.guest_agent.0 --blacklist=guest-file-open,guest-file-close,guest-file-read,guest-file-write,guest-file-seek,guest-file-flush,guest-exec,guest-exec-status -F/etc/qemu-ga/fsfreeze-hook
 0.0   669 avahi    avahi-daemon: running [devprocsys.local]
 0.0   668 root     /usr/sbin/rsyslogd -n
 0.0   667 root     /usr/sbin/ModemManager
 0.0   666 root     /usr/lib/systemd/systemd-logind
 0.0   665 root     /usr/sbin/irqbalance --foreground
 0.0   664 root     /usr/sbin/smartd -n -q never
 0.0   662 libstor+ /usr/bin/lsmd -d
 0.0    65 root     [deferwq]
 0.0   644 root     /usr/sbin/sedispatch
 0.0   642 root     /sbin/audispd
```