#!/usr/bin/env python3

## NOTE that this works on the LINUX Virtual Lab Environment

## You can get it to work in the Windows Pycharm Environment
## by Settings: Project Interpreter:
## then install packages, look for netifaces

import netifaces

print(netifaces.interfaces())

# Loop through each network interfaces
for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')

    # This prints out a list that contains a dictionary
    # Keys include: 'addr', 'broadcast', or 'peer'
    # print(netifaces.ifaddresses(i)[netifaces.AF_LINK])

    # This prints out the MAC address given, using the key 'addr'
    # print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])

    # This also prints out the IP address, using the key 'addr'
    # print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    try:
        print('MAC: ', end='')  # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr'])  # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr'])  # Prints the IP address
    except:  # This is a new line
        print('Could not collect adapter information')  # Print an error message
