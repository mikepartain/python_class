#!/Users/mikepartain/git-hub/python/bin/python
'''
This script is just to show some basic examples of using Netmiko to login to devices.
This script will login to a single device with cisco/cisco and run the show ip int brief
command.  It will then run show run | section line.
'''
config_dir = 'configs/'
import os
from netmiko import ConnectHandler
os.system('clear')


ios = {
        'device_type': 'cisco_ios',
        'ip': '192.168.178.28',
        'username': 'cisco',
        'password': 'cisco',
    }


def device_login():
    global net_connect, hostname, running_config
    net_connect = ConnectHandler(**ios)
    hostname = net_connect.find_prompt().replace('#','')
    print 'Connected to: '+  net_connect.find_prompt().replace('#','')
    running_config = open(config_dir+hostname, 'w')

def get_device_config():
    config = net_connect.send_command('show run')
    running_config.write(config)
    

def get_interfaces():
    print '#'*30+'Show IP Interface Brief'+'#'*30
    interfaces = net_connect.send_command('show ip int brief')
    print interfaces
    
def get_line_config():
    print '\n\n'
    print '#'*30+'Show run | section line'+'#'*30
    line_config = net_connect.send_command('show run | section line')
    print line_config

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
get_device_config()
get_interfaces()
get_line_config()
net_disconnect()
