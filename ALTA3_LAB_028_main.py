#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""


# function to push commands
def commandpush(devicecmd):  # devicecmd == dictionary
    # my_ip_key is used in the loop, it could be renamed something else
    # my_ip_key is used to access each key-value in the dictionary
    for my_ip_key in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + my_ip_key)
        # we'll learn to write code that connects to devices here

        # Access the value associated with the key, my_ip_key
        # Note that this is a list of commands
        for mycmds in devicecmd[my_ip_key]:
            print('Attempting to sending command --> ' + mycmds)
            # we'll learn to write code that sends cmds to device here


# start our main script
def main():
    # work2do is a dictionary, where the key values are IP addresses
    work2do = {"10.1.0.1": ["interface eth1/2", "no shut"], "10.2.0.1": ["interface eth1/1", "shutdown"],
               "10.3.0.1": ["interface eth1/5", "no shutdown"]}  # data that replaces data stored in file

    print("Welcome to the network device command pusher")  # welcome message

    ## get data set
    print("\nData set found\n")  # replace with function call that reads in data from file

    ## run
    commandpush(work2do)  # call function to push commands to devices


# call our main function
main()