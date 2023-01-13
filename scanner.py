import socket
from IPy import IP

def scan(target):
    try:
        converted_ip = IP(target)
    except ValueError:
        converted_ip = socket.gethostbyname(target)
    print(f'\n[** Scanning Target **] {converted_ip}')
    for port in range(20, 100):
        scan_port(converted_ip, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.create_connection((ipaddress, port), timeout=0.5)
        try:
            banner = sock.recv(1024)
            print(f'[+] Open port {port}: {banner.decode()}')
        except:
            print(f'[+] Open port {port}')

    except (socket.timeout, ConnectionRefusedError, OSError) as e:
        pass

targets = input("[+] Enter target/s to scan (split multiple targets with ','):")
for target in targets.split(','):
    scan(target.strip())
