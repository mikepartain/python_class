#!/Users/mikepartain/git-hub/python/bin/python
'''
This script will push an ACL to a single device.  The ACL is stored in templates/ACL,
it will login and copy the lines in the script to the device it is connected to.
'''
config_dir = 'configs/'
import os
from netmiko import ConnectHandler
os.system('clear')

ios = {
        'device_type': 'cisco_ios',
        'ip': '172.16.5.101',
        'username': 'cisco',
        'password': 'cisco',
    }


def device_login():
    global net_connect, hostname, running_config
    net_connect = ConnectHandler(**ios)
    hostname = net_connect.find_prompt().replace('#','')
    print 'Connected to: '+  net_connect.find_prompt().replace('#','')
    running_config = open(config_dir+hostname, 'w')


def push_acl():
    ACL = 'templates/ACL'
    print 'Attempting to push %s to %s' % (ACL, hostname)
    net_connect.config_mode()
    net_connect.send_config_from_file(ACL)


def get_device_configs():
    #list the configs
    for device in os.listdir(config_dir):
        print device


def net_disconnect():
    print '\n\n'
    print '#'*30+'Disconnecting from host'+'#'*30
    print 'Disconnecting from %s...' % (hostname)
    net_connect.disconnect()



device_login()
push_acl()
#get_device_config()
net_disconnect()
