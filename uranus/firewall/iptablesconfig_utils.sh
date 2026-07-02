
OPEN_PORT_TCP(){
    local PORT=$1
    iptables -A INPUT -p tcp --dport "$PORT" -j ACCEPT
}

OPEN_PORT_UDP(){
    local PORT=1
    iptables -A INPUT -p udp --dport "$PORT" -j ACCEPT
}

BLOCK_ICMP_NUM(){
    local ICMP_NUM=$1
    iptables -A INPUT -m conntrack -p icmp --icmp-type "$ICMP_NUM" --ctstate NEW,ESTABLISHED,RELATED -j ACCEPT
}