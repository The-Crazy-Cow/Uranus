#!/bin/bash

# ==============================================================================
# 							SECGRUB
# ==============================================================================
# NAME: 
#    secgrub - Secure the GRUB bootloader interface.
#
# SYNOPSIS:
#    sudo ./secgrub.sh
#
# DESCRIPTION:
#    Secures the GRUB interface with two levels of protection:
#    - Normal: Pass-protected editing, free booting.
#    - Max: Pass-protected editing AND booting.
#
#    Execution time: Approx. 2 minutes.
#    Requirements: GRUB 2, grub-mkpasswd-pbkdf2, root privileges.
#
# WARNINGS:
#    This script modifies critical system files (/etc/grub.d/).
#    A backup is automatically created for each modified file.

source ./utils.sh

CHECK_ENV
USER_INPUTS

echo 

hash=$(printf "%s\n%s" "$password" "$password" | grub-mkpasswd-pbkdf2 |grep -o "grub.pbkdf2.*" )
unset password
if [[ -z "$hash" ]]; then
    echo -e "\e[31mError: Failed to generate hash.\e[0m"
    return 1
fi

echo -e "\n\n
	$(printf '#%.0s' {1..7}) made by ${0} script on this date $(date -I) $(printf '#%.0s' {1..7})\n
	set superusers=\"${username}\"\n
	password_pbkdf2 ${username} ${hash}\n
	$(printf '#%.0s' {1..7})" >> "$custom_file"

#make backup
echo -e "\e[34m[Backup]\e[0m backup of $linux_file...."
backup_file="${linux_file}_$(date -I).back"
#save rights
cp -p "$linux_file" "$backup_file"
echo -e "$(printf '#%.0s' {1..7}) backup made by ${0##*/} $(printf '#%.0s' {1..7})\n" | cat - "$backup_file" > "${backup_file}.tmp" && mv "${backup_file}.tmp" "$backup_file"

if [ "$security_level" == "N" ]; then
    echo -e "\033[32m\nConfiguration of grub with maximal security (unrestricted mode )...\033[0m"
    # make unsrestricted
    sed -i '0,/CLASS="/ s/\(CLASS="[^"]*\)"/\1 --unrestricted"/' "$linux_file"
else
	echo -e "\033[32m\nConfiguration of grub with maximal security (restricted mode )...\033[0m"
	sed -i 's/\(CLASS="[^"]*\) --unrestricted\(".*\)/\1\2/' "$linux_file"
fi

if grub-mkconfig -o /boot/grub/grub.cfg > /dev/null 2>&1; then
    echo "\033[32m\nSuccess: ✔ GRUB configuration updated.\033[0m"
    return 0
else 
    echo -e  "\e[31mError : ✘ Failed to update GRUB.\e[0m"
    return 1
fi


###########SEE ALSO :
##########
##########
##########
# AUTHOR:  aliceQueelImpress
# VERSION: 1.0
# E-MAIL:  jdj17180@gmail.com
# DATE:    2026-02-23
# ==============================================================================