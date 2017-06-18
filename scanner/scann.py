#!/Users/mikepartain/git-hub/python/bin/python
from scapy.all import *
from netaddr import *
import sys
from datetime import datetime

def main():
    try:
        network = raw_input('What network would you like to scan? (ie 192.168.1.0/24): ')
        if IPNetwork(network):
            print 'Valid network entered.'
            scan(network)
        else:
            print 'Invalid network, please try again'
            main()

    except KeyboardInterrupt:
        print '\nExiting due to user break.'

    except AddrFormatError:
        print 'Invalid network, please try again'
        main()


def scan(network):
    starttime = datetime.now()
    print 'Starting scan at: ', starttime
    conf.verb = 0
    for ip in IPNetwork(network).iter_hosts():
        packet = IP(dst=ip, ttl=20) / ICMP()
        reply = sr1(packet)
        if ip in reply.src:
            print reply.src +' is online.'
    #     print '%s' % ip


main()
