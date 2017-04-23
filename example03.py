#!/home/mikepartain/GIT/stig/bin/python
'''
This script will interact with two three IOS devices and one IOS-XR based on the 
list of devices that are in the device_list.txt file in the local directory.
The script will login and set the hostname to what is in the device_list.txt file.

'''
config_dir = 'configs/'
import os
from netmiko import ConnectHandler
os.system('clear')


def get_device_list():
    global dev_hostname, dev_type, dev_ip, ios
    for line in open('device_list.txt', 'r'):
        line = line.strip('\n')
        dev_hostname = line.split(',',-1)[0].strip()
        dev_type = line.split(',',-1)[1].strip()
        dev_ip = line.split(',',-1)[2].strip()
        #print dev_hostname, dev_type, dev_ip
        if dev_type == 'XR':
            print 'Attempting to login to %s which is an %s device.' % (dev_hostname, dev_type)
            ios = {
            'device_type': 'cisco_xr',
            'ip': dev_ip,
            'username': 'cisco',
            'password': 'cisco',
            }
            xr_device_login()
            xr_set_hostname(dev_hostname)
            net_disconnect()

        elif dev_type == 'IOS':
            print 'Attempting to login to %s which is an %s device.' % (dev_hostname, dev_type)
            ios = {
                    'device_type': 'cisco_ios',
                    'ip': dev_ip,
                    'username': 'cisco',
                    'password': 'cisco',
                }
            ios_device_login()
            ios_set_hostname(dev_hostname)
            net_disconnect()
        else:
            print 'Error, couldnt detect device type.'
            os.system('exit')


def ios_device_login():
    print '#'*30+'Logging into %s' % (dev_hostname)+'#'*30
    global net_connect, hostname, running_config
    net_connect = ConnectHandler(**ios)
    hostname = net_connect.find_prompt().replace('#','')
    print 'Connected to: '+  net_connect.find_prompt().replace('#','')
    #running_config = open(config_dir+hostname, 'w')

def xr_device_login():
    global net_connect, hostname, running_config
    net_connect = ConnectHandler(**ios)
    hostname = net_connect.find_prompt().replace('#','').split(':',-1)[1]
    print 'Connected to: '+  net_connect.find_prompt().replace('#','')
    #running_config = open(config_dir+hostname, 'w')

def ios_set_hostname(dev_hostname):
    net_connect.config_mode()
    #print net_connect.check_config_mode()
    print 'Setting %s\'s hostname to %s' % (hostname, dev_hostname)
    output = net_connect.send_config_set(['hostname '+dev_hostname, 'end'])
    net_connect.send_command('write mem')
    print output

def xr_set_hostname(dev_hostname):
    output = net_connect.send_config_set(['hostname '+dev_hostname, 'commit'])
    print(output)


def net_disconnect():
    print '#'*30+'Disconnecting from host'+'#'*30
    print 'Disconnecting from %s...' % (hostname)
    net_connect.disconnect()
    print '\n\n'


get_device_list()
