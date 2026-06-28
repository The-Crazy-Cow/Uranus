






# see (L105)
man -k monitor or man -k performance <=> apropos ....

+-----------------------------------------------------------+
+                   SAR ( System Activity Reporter:L137)    +
+-----------------------------------------------------------+

# package : sysstat
by default the sar by sadc (System Activity Data Collector) utility uses data stored in utility in /var/log/sa/

# in the /var/log/sa/
saXX : binary files and sarXX : text file generated based on binary files (xx represent the day of the mount)

sar -f /var/log/sa/sa15 #afficher un fichier specific
sar -f /var/log/sa/sa15 -s 14:00:00 -e 15:30:00 #filter
sar -A -f /var/log/sa/sa15 #pr
sar 1 4 #intervall of and print  4 ; by default is 10 seconds

# config => set_sar.sh
On a Debian-based distribution, modify 
the file /etc/default/sysstat and set ENABLED="true" or sudo dpkg-reconfigure sysstat

read /etc/sysstat/sysstat file for make any personnal conf 
sysstat-summary.service calls /usr/lib/sysstat/sa2 script (man 8 sa2) generated the sarr rapport files and log ratation of 
the current data stored directory => systemctl list-timers | grep sysstat-summary

systemctl enable sysstat

+-----------------------------------------------------------+
+                       SEE ALSO                            +
+-----------------------------------------------------------+