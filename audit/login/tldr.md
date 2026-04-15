1- Manage login console or gui check  /etc/issue;/etc/motd;/etc/issue.net (L102)

2- /etc/motd is print after the login:ideal for communicate some information  and 
/etc/issue.net is printing before the login:ideal for warinings (specially for ssh protocol)

3- about the sshd config :Remove the hash mark (#) from the line. If the word none is listed, instead of the issue 
.net file, change it to /etc/issue.net => "#banner none"  to  "banner /etc/issue.net"

4- check the file : /etc/login.defs == configuration file of user and groups mechanism

.set the usmask to 0077 in /etc/login.defs and $ cd /home && chmod 0077 *

+-----------------------------------------------------------+
+  THE ROOT LOGIN CASE : S U D O
+-----------------------------------------------------------+
!!!!prefer add file in etc/sudoers.d/ directory 

7- by default the sudo timer = 5 minutes: sudo -k to reinitialise it or sudo -K
for persistant: in sudoers file : Defaults env_reset, timestamp_timeout=X (0:0 minutes; -1: ne périme jamais le token)
or Defaults:<user_name> timestamp_timeout=30 #define for an user

=> Defaults env_reset, timestamp_timeout

8- sudo -l : check my rights in sudoers file

#use sudo <cmd>  => can trace but with su - or sudo su - don't no exactly who connect as root and perform some actions

#add the user to the wheel group and edit the /etc/sudoers file with visudo : %wheel ALL(ALL:ALL) ALL and check with visudo -c

#you will see perharps %whell ALL (ALL:ALL) NOPASSWD:ALL : it's not recommanded => system not check the user identity with his password
#before accord him root rights

#to define alias
User_Alias #for user
Runas_Alias  #for groups
Host_Alias  #machines
Cmnd_Alias #command

DEVS ALL = (ALL) !/bin/su  #forbiden the su command

#recall use of visudo : -c : check ; -f specify path of the conf sudoers file (rarely use)

%wheel ALL (ALL:ALL) 
note : usermod -aG wheel bob 
sudo useradd -G wheel -m -d /home/<user_name> -s /bin/bash <user_name>

at the end : sudo passwd -l root #lock root account (add ! in the /etc/shadow line for root) 
and check with : sudo -S root #it's really lock ? L = Lock and P = Password = actif

---------------------
       forbidenns 
---------------------

maggie ALL=(ALL) /bin/bash, /bin/zsh 
#the use of sudoedit for prevent shell escape
franckl ALL=(ALL) /bin/vim /etc/file ; instead prefer ; franckl ALL=(ALL) sudoedit /etc/file
alice ALL=(ALL:ALL) /usr/bin/systemctl status *
be aware also with the use of cat,sed,awk,etc...

perfer ------ myke ALL=(<username>:<group>) <specific path> -------------
*prevent the ownershhip => myke and user and group rights on path

+---------------------------------------------------------------------------+
+                       USER AND GROUPS                                     +
+---------------------------------------------------------------------------+
IV- Be Aware of adduser : by default create user home with wide open 755 mask
=>set in /etc/adduser.conf DIR_MODE=0700
=>;see also for password case :PASS_MAX_DAYS;PASS_MIN_DAYS,PASS_WARN_AGE

.for encryption with adduser and ecryptfs-utils see MLH:80

.for password => MLH83 also libpam-pwquality paquet and pwquality on centOs

View user expiry account data : chage -l <username>

+-----------------------
    ecryptfs-utils
+-----------------------



+-----------------------------------------------------------+
+                       SEE ALSO                            
+-----------------------------------------------------------+
L(106) => ubuntu case