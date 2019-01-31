#!/usr/bin/env python3
loginfail = 0
loginsuccess = 0

# Uncomment this line if you are running this in the LINUX virtual lab environment
#keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi','r')


# Uncomment this line if you are running this in the Windows environment on your local machine
keystone_file = open('keystone.common.wsgi','r')


############################################################################################################
# PROBLEM:  The string 'Authorization failed' appears for both FAILED and SUCCESSFUL login attempts
#
# If the string "- - - - -] Authorization failed" appears . . . you know that it is a FAILED login
# If that string does not appear, it may still be a successful login attempt!!!
#
# Thus the "elif" statement for "-] Authorization failed" may be also found, showing an successful login
# If the order of the if/elif would be switched, then it would return all SUCCESSFUL logins!!!
############################################################################################################
# TRY THIS . . .
# The correct method is . . . Don't comment lines 33 and 40
#
# You will get incorrect results if you comment 33, 40 and UNCOMMENT 32 and 39
################################################################################
keystone_file_lines=keystone_file.readlines()

for i in range(len(keystone_file_lines)):
    tmp_line = keystone_file_lines[i]

    #if "-] Authorization failed" in keystone_file_lines[i]:
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
        loginfail += 1 # this is the same as loginfail = loginfail + 1

        temp,ipaddress = tmp_line.split("from")
        print('Failed attempt from ip', ipaddress)
        print(tmp_line)
    #elif "- - - - -] Authorization failed" in keystone_file_lines[i]:
    elif "-] Authorization failed" in keystone_file_lines[i]:
        loginsuccess += 1
        print('Successful attempt')
        print(tmp_line)

print('The number of failed log in attempts is ' + str(loginfail))
print('The number of successful log in attempts is ' + str(loginsuccess))

## You should have 3 failed log in attempts
## You should have 1 successful log in attempts