import sys
from modules.recon import recon
if len(sys.argv) < 2:
    print("Usage: python main.py <url>")
    sys.exit(1)
url = sys.argv[1]
if not url.startswith('http://'):
    url = 'https://' + url
ip = recon(url)