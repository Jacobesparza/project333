import socket
from datetime import datetime


def scan_ports(target, start_port, end_port):
    """Scans a range of ports on a target host and identifies open ports."""
    print(f"Starting scan on host: {target}")
    start_time = datetime.now()

    open_ports = []

    try:
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((target, port))
                if result == 0:
                    print(f"Port {port}: Open")
                    open_ports.append(port)
                else:
                    print(f"Port {port}: Closed")
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
    except socket.gaierror:
        print("\nHostname could not be resolved.")
    except socket.error:
        print("\nCouldn't connect to server.")

    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"\nScan completed in: {total_time}")
    print(f"Open ports: {open_ports}")


def validate_ports(start_port, end_port):
    """Validates the port range provided by the user."""
    if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
        raise ValueError("Port numbers must be between 1 and 65535.")
    if start_port > end_port:
        raise ValueError("Start port must be less than or equal to end port.")


if __name__ == "__main__":
    # Define the target host and port range
    target_host = "localhost"  # Change to "scanme.nmap.org" for scanning the nmap test site
    start_port = 1
    end_port = 500

    try:
        validate_ports(start_port, end_port)
        scan_ports(target_host, start_port, end_port)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")