#!/Users/mikepartain/git-hub/python/bin/python
from netaddr import *
from scapy.all import *
import pcapy
network = '192.168.178.0/29'
ports = range(1,100)
SYNACK = 0x12
RSTACK = 0x14
hosts = []
def ping_sweep():
    for ip in IPNetwork(network).iter_hosts():
        conf.verb = 0
        #print 'Scanning IP: %s' % (ip)
        ip = str(ip)
        global target
        target = ip
        packet = IP(dst=ip, ttl=20)/ICMP()
        reply = sr1(packet, timeout=1)
        if not (reply is None):
            print ip, 'is online'
            if ip not in hosts:
                hosts.append(ip)
            check_host(ip)
        else:
            print ip, 'is not online'
    
def scan_port(port):
    srcport = RandShort()
    #print 'SRC Port:', srcport
    conf.verb = 0
    SA = sr1(IP(dst = target)/TCP(sport = srcport, dport = port, flags = 'S'))
    pktflags = SA.getlayer(TCP).flags
    #print pktflags
    if pktflags == SYNACK:
        return True
    else:
        return False

def check_host(host):
    for port in ports:
        #print port
        status = scan_port(port)
        if status == True:
            print 'Port: %s is open.' % (port)


ping_sweep()
