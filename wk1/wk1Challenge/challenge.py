"""DevNet High - Class of 2020 - Challenge 1"""

import random
import ipaddress

# TODO: Write a print statement that displays both the type and value of 'ip'
ip = "10.1.1.200"

print(f'The IP is: {ip} and the type is {type(ip)}')




# TODO: Write a conditional to print out if `iosversion` is less than or greater than 14
i = random.randint(12, 17)
print('i is {}'.format(i))
if i>14:
    print(f'The IOS version is greater than 14')

# TODO: Write a conditional that prints the serial number of the device
devices = ({'CAT9300':'XVNM1245ERGC'}, {'ISR4331':'VNMM8742THBX'}, {'NGFW2120':'EAQP4900RTJO'})
device = random.sample(devices, 1) [0]
#device2 = list(device.values())[0]
for key in device:
    device_model = key
    device_serial = device[key]

print(f'The Serial is: {device_serial} and the device model is {device_model}')

# Function for converting CIDR notation into 32-bit netmask (nothing to do here)
def cidr_to_netmask(ip_str):
    ip = ipaddress.IPv4Network(ip_str)
    return ip.with_netmask

'''
TODO: Call the function above few times to so that the input of IP network with CIDR displays the IP network with 32-bit netmask
Example:
Input would be '10.1.1.0/24' and when printed out the output would be '10.1.1.0/255.255.255.0'
'''
ip_a = '10.1.1.0/24'
ip_b = '10.1.0.0/16'
ip_c = '10.1.1.0/24'

while True:
    try:
        address_input = input("Enter the IP network and mask in CIDR format: ")
        if ipaddress.IPv4Network(address_input):
            break
    except Exception as e:
            print(e)

print(f'The IP input is {ip_a} and the CIDR Netmask output is {cidr_to_netmask(ip_a)}')

print(f'The IP input is {ip_b} and the CIDR Netmask output is {cidr_to_netmask(ip_b)}')

print(f'The IP input is {ip_c} and the CIDR Netmask output is {cidr_to_netmask(ip_c)}')

print(f'The IP input is {address_input} and the CIDR Netmask output is {cidr_to_netmask(address_input)}')
