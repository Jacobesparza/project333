#!/bin/bash

# List of servers to configure
# Replace these with your actual server addresses
SERVERS=("server1.example.com" "server2.example.com" "server3.example.com")

# SSH user
# Replace 'your-username' with your actual SSH username
USER="your-username"

# Firewall rules
# An associative array where keys are rule names and values are the corresponding ufw commands
declare -A RULES
RULES=(
  ["allow_ssh"]="ufw allow 22/tcp"             # Allow SSH
  ["allow_http"]="ufw allow 80/tcp"            # Allow HTTP
  ["allow_https"]="ufw allow 443/tcp"          # Allow HTTPS
  ["deny_all_incoming"]="ufw default deny incoming"  # Deny all incoming traffic by default
  ["allow_all_outgoing"]="ufw default allow outgoing" # Allow all outgoing traffic by default
)

# Function to apply firewall rules on a server
# Takes one argument: server address
apply_firewall_rules() {
  local server=$1
  echo "Configuring firewall on ${server}..."

  # Iterate over the RULES array and apply each rule
  for rule in "${!RULES[@]}"; do
    ssh "${USER}@${server}" "${RULES[$rule]}"
  done

  # Enable the firewall
  ssh "${USER}@${server}" "ufw enable -y"
  echo "Firewall configured on ${server}."
}

# Main script execution
# Iterate over the list of servers and apply firewall rules to each
for server in "${SERVERS[@]}"; do
  apply_firewall_rules "${server}"
done

echo "Firewall configuration completed on all servers."