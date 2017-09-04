#!/Users/mikepartain/git-hub/python/bin/python
from ciscoconfparse import *


for file in os.listdir('configs/'):
    parse = CiscoConfParse('configs/'+file, factory=True)
    print file

    interfaces = parse.find_interface_objects('Ethernet')

    for interface in interfaces:
        print interface