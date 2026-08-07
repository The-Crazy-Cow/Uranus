#!/bin/bash

# ==============================================================================
# 		                       I P T A B L E S C O N F I G
# ==============================================================================
# NAME: 
#    iptablesconfig - iptables configuration
#
# SYNOPSIS:
#    script for config iptables firewall rules
#
# DESCRIPTION:
#       -------------
#
# WARNINGS:
#       script should be run in root mode
#       tips: iptables rules are processed in order, from top  to bottom, any 'ACCEPT' 
#       rules that come after that 'DROP' or 'REJECT' rule woule have no effect

#TODO: verify user login as root : EUID=0

#verify iptables installed

source ./iptablesconfig_utils.sh

SSH_PORT="${SSH_PORT:-22}"
#DNS_PORT

#pass incoming packets from servers that we have requested connection
iptables -A INPUT  -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

#open port for ssh
OPEN_PORT_TCP "$SSH_PORT"

# dns server : port 853 for secure dns 
if [[ ! -z "$DNS_PORT" ]]; then
    OPEN_PORT_TCP "$DNS_PORT"
    OPEN_PORT_UDP "$DNS_PORT"
fi

#the loopback interface for hostname resolution 
iptables -I INPUT 1 -i lo -j ACCEPT

#blocking icmp 
BLOCK_ICMP_NUM "3"
BLOCK_ICMP_NUM "5" #del it if you are on server connect to internet
BLOCK_ICMP_NUM "11"
BLOCK_ICMP_NUM "12"

# use drop to ensure invisble
iptables -A INPUT -j DROP
iptables -P INPUT DROP

#persitence










