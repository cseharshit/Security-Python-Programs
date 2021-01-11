import nmap
import sys
import getopt

class PortScan:
    def __init__(self, target, *args):
        self.target = target
        if type(args[0]) is list:
            self.ports = args[0]
        else:
            self.ports = list(args)

    def port_scan(self):
        scanner = nmap.PortScanner()
        port_status={}
        for port in self.ports:
            portscan = scanner.scan(self.target, str(port))
            port_status[port] = portscan['scan'][list(portscan['scan'])[0]]['tcp'][port]['state']
        return port_status ,  portscan['scan'][list(portscan['scan'])[0]]['status']['state']


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print ("Usage: " + "python3 "+ sys.argv[0].split('/')[-1]+" <host> <port(s)> ")
        sys.exit(1)
    target = str(sys.argv[1])
    cmd_args = sys.argv
    port_args = list(map(int,cmd_args[2:]))
    portscanner = PortScan(target,port_args)
    port_status, host_status = portscanner.port_scan()
    print("Host status = ",host_status)
    for port,status in port_status.items():
        print("Port {} is {}".format(port,status))