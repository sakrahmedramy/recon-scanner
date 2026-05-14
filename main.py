import sys
from modules.recon import recon

url = sys.argv[1]
if not url.startswith('http://'):
    url = 'https://' + url
ip = recon(url)