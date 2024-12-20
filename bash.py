#!/bin/bash

# List of servers to manage (replace with your actual server IPs or hostnames)
SERVERS = ("server1.example.com" "server2.example.com" "server3.example.com")
# SSH user
SSH_USER = "your_ssh_user"

# Function to apply firewall rules on a server
apply_firewall_rules()
{
    local
server = "$1"

echo
"Applying firewall rules on $server..."

ssh
"$SSH_USER@$server" << 'EOF'
# Enable UFW
sudo
ufw
enable

# Reset all rules to default
sudo
ufw
reset

# Allow SSH (port 22)
sudo
ufw
allow
22

# Example: Allow HTTP (port 80)
sudo
ufw
allow
80

# Example: Allow HTTPS (port 443)
sudo
ufw
allow
443

# Example: Deny all incoming traffic by default
sudo
ufw
default
deny
incoming

# Example: Allow all outgoing traffic by default
sudo
ufw
default
allow
outgoing

# Reload UFW to apply changes
sudo
ufw
reload

echo
"Firewall rules applied on $server."
EOF
}

# Loop through the servers and apply firewall rules
for server in "${SERVERS[@]}"; do
apply_firewall_rules
"$server"
done

echo
"Firewall setup and management completed on all servers."