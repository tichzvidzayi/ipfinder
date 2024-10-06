import socket

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"IP address of {domain} is: {ip}")
    except socket.gaierror:
        print(f"Unable to get IP address for {domain}")

if __name__ == "__main__":
    domain = input("Enter a domain name: ")
    get_ip(domain)
