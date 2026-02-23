
BANNER() {
    # Codes couleurs
    local RED='\e[31m'
    local GREEN='\e[32m'
    local BOLD='\e[1m'
    local RESET='\e[0m'

    echo -e "${BOLD}"
    echo -e "${RED} ___  ____ ____ ${GREEN} ____ ____  _   _ ____ "
    echo -e "${RED}/ __|| ___/ ___|${GREEN}/ ___|  _ \| | | | __ )"
    echo -e "${RED}\__ \|  _|| |   ${GREEN}| |  | |_) | | | |  _ \\"
    echo -e "${RED} ___) | |__| |__ ${GREEN}| |__|  _ <| |_| | |_) |"
    echo -e "${RED}|____/|_____\____${GREEN}\____|_| \_\\___/|____/"
    echo -e "${RESET}"
    echo -e "  ${RED}SEC${RESET}${GREEN}GRUB${RESET} Security Hardening Tool"
    echo -e "\e[90m------------------------------------\e[0m\n"
}

CHECK_ENV(){

	if [ "$EUID" -ne 0 ];then
		echo -e "\e[31mError : permission denied.\e[0m"
		echo
		return 1
	fi

	file_exit () {
		local file=$1

		if [ ! -f "$file" ];then
			echo -e "${file} doesn't exist !\n"
			read -p "Créé le fichier ${file} [Y/N] ?" -n 1 -r
			echo

			if [[ $REPLY =~ ^[Yy]$ ]];then
				echo "creation du fichier ${file}... }"
				touch "$file"
			else
				return 1
			fi
		else
			if [ ! -x "$file" ];then
				echo -e  "${file} doesn't have the 'x' right !\n"
				read -p "Add 'x' right to file ${file} [Y/N] ?" -n -r
				echo

				if [[ $REPLY =~ ^[Yy]$ ]];then
					echo "adding 'x' right to file ${file}..."
					chmod 700 "$file"
				else
					return 1
				fi
			fi
		fi

	}

	check_command(){
		local cmd=$1

		if ! command -v "$cmd" &> /dev/null 2>&1;then
            echo -e "\e[31mError :${cmd} not found in \$PATH .\e[0m"
            echo
            return 1
		fi
	}

	custom_file="/etc/grub.d/40_custom"
	linux_file="/etc/grub.d/10_linux"
	file_exit "$custom_file" || return 1
	file_exit "$linux_file" || return 1

	check_command grub-mkpasswd-pbkdf2 || return 1
	check_command grub-mkconfig || return 1
}

USER_INPUTS (){
	ask_password() {
		local pass1 pass2
		
		while true; do
			read -rs -p "Enter the password : " pass1
			echo
			read -rs -p "Confirm the password : " pass2
			echo
			
			if [[ ! "$pass1" == "$pass2" ]]; then
				echo -e "\e[31mError : Passwords don't match. Retry.\e[0m"
				echo
			else
				password="$pass1"
				break
			fi
		done
	}

	set_security_level (){
		while true; do
		read -p "Niveau de sécurité [N]ormal ou [M]ax : " security_level
		echo
		
		[[ -z "$security_level" ]] && security_level="N"
		
		#to upper
		security_level=${security_level^^}

		if [[ "$security_level" == "N" || "$security_level" == "M" ]]; then
			break
		else
			echo -e "\e[31mError : Invalid security level. Retry.\e[0m"
			echo 
		fi
	    done

	}

	set_user_name() {
		local target_user
		
		while true; do
			read -p "Enter the username (default is 'root' ) : " target_user
			echo
			
			if [[ -z "$target_user" ]]; then
				username="root"
				break
			fi

			if getent passwd "$target_user" > /dev/null 2>&1; then
				username="$target_user"
				break 
			else
				echo -e "\e[31mError : User '$target_user' not found in /etc/passwd.\e[0m"
				echo
			fi
		done
	}

    set_security_level
    set_user_name
    ask_password

}

MAIN(){
    BANNER
    CHECK_ENV || exit 1
    USER_INPUTS
}

MAIN
