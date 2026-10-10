
import socket

# Only scan a device you own or have permission to test.
target = input("Enter target IP address: ").strip()

ports = [22, 80, 443, 8080]

warnings = {
    22: "SSH is open. Enforce strong authentication.",
    80: "HTTP is open. Check whether HTTPS is appropriate.",
    443: "HTTPS is open. Check TLS configuration."
}

for port in ports:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))

            if result == 0:
                print(f"Port {port}: OPEN")

                if port in warnings:
                    print(f"  Warning: {warnings[port]}")
                    
            else:
                print(f"Port {port}: CLOSED or FILTERED")

    except OSError as error:
        print(f"Port {port}: Error - {error}")
