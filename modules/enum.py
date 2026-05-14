from modules.recon import recon

ip = recon()

nm.scan(hosts=ip,arguments='-sV -O -F --randomize_hosts')