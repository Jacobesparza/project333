# Firewall Configuration Automation

## Project Objectives

The Firewall Configuration Automation project aims to automate the setup and management of firewall rules across multiple servers. This project uses a Bash script to ensure that specific firewall rules are consistently applied to all designated servers, enhancing security and simplifying the management process.

## Features

- **Automated Firewall Setup**: Automatically configure firewall rules on multiple servers.
- **Rule Consistency**: Ensure that all servers have the same set of firewall rules.
- **Scalability**: Easily add or remove servers from the configuration list.
- **Customizable Rules**: Modify the firewall rules as needed to fit your security requirements.

## Setup Instructions

### Prerequisites

- **SSH Access**: Ensure you have SSH access to all the servers you want to configure.
- **`ufw` Installed**: The `ufw` (Uncomplicated Firewall) tool must be installed on each server.
- **Bash**: The script should be run in a Unix-like environment with Bash.

### Dependencies

- **Bash**: The script is written in Bash, which is available on most Unix-like systems.

### Configuration

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/firewall-automation.git
    cd firewall-automation
    ```

2. **Edit the Script**:
    - Open the `configure_firewall.sh` script in your favorite text editor.
    - Update the `SERVERS` array with the hostnames or IP addresses of your servers.
    - Update the `USER` variable with your SSH username.
    - Modify the `RULES` associative array to customize the firewall rules as needed.

3. **Make the Script Executable**:
    ```bash
    chmod +x configure_firewall.sh
    ```

4. **Run the Script**:
    ```bash
    ./configure_firewall.sh
    ```

## Example Script

### `configure_firewall.sh`

```bash
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