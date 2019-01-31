#!/usr/bin/env python3

outFile = open('admin.rc', 'a')

# Prompt the user for the OS_AUTH_URL
print('What is the OS_AUTH_URL?')
osAUTH = input()
print('export OS_AUTH_URL=' + osAUTH, file=outFile)

print('export OS_IDENTITY_API_VERSION=3', file=outFile)
print('What is the OS_PROJECT_NAME?')

# Prompt the user for the OS_PROJECT_NAME
osPROJ = input()
print('export OS_PROJECT_NAME=' + osPROJ, file=outFile)

# Prompt the user for the OS_PROJECT_DOMAIN_NAME
print('What is the OS_PROJECT_DOMAIN_NAME?')
osPROJDOM = input()
print('export OS_PROJECT_DOMAIN_NAME=' + osPROJDOM, file=outFile)

# Prompt the user for the OS_USERNAME
print('What is the OS_USERNAME?')
osUSER = input()
print('export OS_USERNAME=' + osUSER, file=outFile)

# Prompt the user for the OS_USER_DOMAIN_NAME
print('What is the OS_USER_DOMAIN_NAME?')
osUSERDOM = input()
print('export OS_USER_DOMAIN_NAME=' + osUSERDOM, file=outFile)

# Prompt the user for the OS_PASSWORD
print('What is the OS_PASSWORD?')
osPASS = input()
print('export OS_PASSWORD=' + osPASS, file=outFile)

# Close the file
outFile.close()