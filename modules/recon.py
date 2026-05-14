import requests
import socket
from urllib.parse import urlparse
def recon(url):
    print(f"DEBUG url: {url}")
    r = requests.get(url)
    domain = urlparse(url).netloc
    ip=socket.gethostbyname(domain)
    print(f"IP Address: {ip}")
    print(f"Status code: {r.status_code}")
    return ip
