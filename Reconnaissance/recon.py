import sys
import requests
import socket
import json
import re

class Recon:
    def __init__(self,hostname):
        if hostname.startswith('http'):
            hostname = re.sub(r'https?:\\', '', hostname)
        if hostname.startswith('www.'):
            hostname = re.sub(r'www.', '', hostname)
        self.hostname = hostname

    def get_ip_address(self):
        self.host_by = (socket.gethostbyname(self.hostname))
        return self.host_by

    def get_request_headers(self):
        req= requests.get('https://'+self.hostname)
        return str(req.headers)
    
    def get_ip_info(self):
        ip_info = requests.get("https://ipinfo.io/"+self.host_by)
        return json.loads(ip_info.text)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print ("Usage: " + "python3 "+ sys.argv[0].split('/')[-1]+" <url>")
        sys.exit(1)

    hostname=sys.argv[1]
    recon = Recon(hostname)
    print("\n\n IP Address:\t",recon.get_ip_address(),"\n","-"*10)
    print()
    print(" Request Headers","\n","-"*17,"\n", recon.get_request_headers())
    print()
    print(" IP Info","\n","-"*8,"\n")
    ip_info = recon.get_ip_info()
    print()

    print("Location: "+ip_info["loc"])
    print("Region: ", ip_info["region"])
    print("City: ", ip_info["city"])
    print("Country: ", ip_info["country"])
    print()