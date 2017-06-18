# python_class
Scripts to review during the Python Class

I am using EVE-NG with a basic topology, 1 - IOL, 1 - L3 vIOS, 1, - L2 vIOS, and 1 - IOSXRv
All devices are set for DHCP and connected to a cloud network.  There is a device_list.txt
file that contains the following:
R1, IOS, 192.168.178.28
R2, IOS, 192.168.178.97
SW1, IOS, 192.168.178.99
XR1, XR, 192.168.178.61

There is also a directory called templates that have two ACLs, one for IOS and one for XR.

-- Example01
This script is just to show some basic examples of using Netmiko to login to devices.
This script will login to a single device with cisco/cisco and run the show ip int brief
command.  It will then run show run | section line.


-- Example02
This script will push an ACL to a single device.  The ACL is stored in templates/ACL,
it will login and copy the lines in the script to the device it is connected to.

-- Example03
This script will interact with two three IOS devices and one IOS-XR based on the 
list of devices that are in the device_list.txt file in the local directory.
The script will login and set the hostname to what is in the device_list.txt file.


-- Example04
This script will interact with two three IOS devices and one IOS-XR based on the 
list of devices that are in the device_list.txt file in the local directory.
The script will login and apply the ACL to the devices in the device_list.txt file.


-- Example05
This script will backup the configs of the devices in the device_list.txt and 
store them int he configs directory.
