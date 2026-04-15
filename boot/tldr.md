#dmesg :print the kernel ring buffer (L60,R116)
#
#
+-----------------------------------------------------------+
+                 GRUB2                                     +
+-----------------------------------------------------------+
#
#keys: e => edit ,c => open command line ,F10 or CTRL-X to save and load after edition
#press MAJ seven seconds to force grub print 
#
#configuration of grub2 (L68) see grub-install,grub-mkconfig and /etc/default/grub
#
#choose serveral kernel version (L83)
#
#add 'single' or 'emergency' (L83)  at linux line in grub to log in single user mode
#and use fsck -y if you are there for rescue mode
#
#login without password => delete 'ro' at end of linux line and add 'rw init=/bin/bash
#
#delete 'quiet' and 'splash' option in the linux line to see details instead of logo
#
#running in any run level : egg 3 multi-user: add 3 to the end of vmlinuz line : GRUB_CMDLINE_LINUX="quiet splash 3"



+-----------------------------------------------------------+
+        L O G S                                            +
+-----------------------------------------------------------+
#/var/log/boot.logx files 



+-----------------------------------------------------------+
+        SECURITY :=> execute "secrub.sh" script            +
+-----------------------------------------------------------+
#
#see also update-grub,grub-install
##############################################
#
#
#secure-boot(L70),(mokutil(L70<secure boot in red)
#
#lsblk to see the ESP partition (often /boot/efi)
#/sys/firmware/efi
#
#systemd (L76)
#
+-----------------------------------------------------------+
+                       SEE ALSO                            +
+-----------------------------------------------------------+
#systemd-analyze time,insmod,blacklist(R122),mokutil(L70<secure boot in red>)
#shutdown,halt,reboot,init
