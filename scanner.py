
import socket

# Only scan a device you own or have permission to test.
target = input("Enter target IP address: ").strip()

ports = [22, 80, 443, 8080]

for port in ports:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))

            if result == 0:
                print(f"Port {port}: OPEN")
            else:
                print(f"Port {port}: CLOSED or FILTERED")

    except OSError as error:
        print(f"Port {port}: Error - {error}")
