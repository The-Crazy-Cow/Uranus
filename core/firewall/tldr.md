# firewall/iptables

- **/etc/iptables/** : configuration files directory

- iptables rules are processed in order, from top to bottom, any ACCEPT rules that come
after that DROP or REJECT rule would have no effect

- diff: REJECT sends messages to the sender after blocking packets while DROP don't
use DROP is important to make your host invisible; view the default DROP policy

- block icmp (port=123)

- tests with nmap scan ->(p133) or check in my **github project**

## persistence
- install package **iptables-persistent** ->(p128)
- **netfilter-persistent** : persistence service

```bash
# do following or install iptables-persistent
iptables-save > rules.v4
cp -a rules.v4 /etc/iptables

# iptables -D : delete from runtime not /etc/iptables/*
systemctl restart netfilter-persistent

# save : require netfilter-persistent
netfilter-persistent save

```

## **recall**: https://help.ubuntu.com/community/IptablesHowTo

```bash
# useful options; support ip6tables 
iptables -t mangle -L -v -n --line-numbers # print rules
iptables -D INPUT 3 # delete rule 3
iptables -t mangle -Z  # reset packet count

# pass incoming packets from servers that our host requested a connection; support ip6tables
iptables  -A INPUT -m conntrack --cstate ESTABLISHED,RELATED -j ACCEPT

# open ssh port (22/2222); support ipv6tables
iptables  -A INPUT -p tcp --dport ssh -j ACCEPT

# allow icmp type 3; you will do the same for type 11,12; mitigate on others 0,8 and 5 ->(p123)
iptables -A INPUT -m conntrack -p icmp --icmp-type 3 --cstate NEW,ESTABLISHED,RELATED -j ACCEPT

# for icmpv6; you will do the same for type 2,3,4 - 128,129 - 130,131,132,143 - 134,135,136,141,142
# - 148,149 - 151,152,153 ->(!p140)
ip6tables -A INPUT -p icmpv6 --icmpv6-type 1 -j ACCEPT

# DROP rule; support ipv6tables
iptables -A INPUT -j DROP

# allow traffic on loopback interface; support ipv6tables 
iptables  -I INPUT 1 -i lo -j ACCEPT  

# blocking invalid packets; support ipv6tables 
iptables -t mangle -A PREROUTING -m conntrack --cstate INVALID -j DROP
iptables -t mangle -A PREROUTING -p tcp ! --syn -m conntrack --cstate NEW -j DROP

# set default DROP policy; support ipv6tables
iptables -p INPUT DROP

```