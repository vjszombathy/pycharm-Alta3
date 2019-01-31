#!/usr/bin/env python3

# This creates multiple adminXX.rc files
# Based on the input file, csv_users.txt

import csv

# Initialize the variable f, which refers to the input file
f = open('csv_users.txt', 'r')

# i is a counter variable, used within the for loop
i = 0

# Process each row in the input file
for row in csv.reader(f):
    i = i + 1

    # This creates a unique file name, using the value of the integer, i
    # %d or %i can be used to insert the value of integer, i
    filename = 'admin.rc%d'%(i,)

    # Another way to initialize the filename would be this . . .
    #filename = 'admin.rc' + str(i)

    # This writes a new file, filename
    rcfile = open(filename, 'w')
    print('export OS_AUTH_URL=' + row[0], file=rcfile)
    print('export OS_IDENTITY_API_VERSION=3', file=rcfile)
    print('export OS_PROJECT_NAME=' + row[1], file=rcfile)
    print('export OS_PROJECT_DOMAIN_NAME=' + row[2], file=rcfile)
    print('export OS_USERNAME=' + row[3], file=rcfile)
    print('export OS_USER_DOMAIN_NAME=' + row[4], file=rcfile)
    print('export OS_PASSWORD=' + row[5], file=rcfile)
rcfile.close()