import socket
from IPy import IP


# socket library enable you to established connection over internet
# using IPy to specify the domain name, as well as the IP address

def scan(target):
    converted_ip = check_ip(target)
    print('\n')
    print(f'[** Scanning Target **] {target}')
    for port in range(20, 120):
        scan_port(converted_ip, port)


def check_ip(ip):
    # if IP address supplied with number or string but with right IP, it returns the IP address,
    # if not, it convert the hostname to its ip ID like from nslookup
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(s):
    return s.recv(1024)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        # this just making the port faster, loosing accuracy but gaining time
        sock.connect((ipaddress, port))
        # this
        try:
            banner = get_banner(sock)
            print(f'[+] Open port {port}: {banner.decode()}')
        except:
            print(f'[+] Open port {port}')

    except:
        pass


if __name__ == '__main__':
    targets = input('[+] Enter target/s to scan: (split multiple targets with ,):')
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)
