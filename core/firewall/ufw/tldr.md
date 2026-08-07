# firewall/ufw

- provide useful learning ->(p145)

- **/etc/ufw/** : configuration files directory

```bash
# enable service
systemctl enable --now ufw

# viewing
ufw status

# open ssh port:will be see in ufw-user-input chain with iptables
ufw allow 22/tcp
# ufw permit 22/tcp

# open port for tcp and udp
ufw allow 53

# enforce rules
ufw enable
ufw reload # after changes were made

```
