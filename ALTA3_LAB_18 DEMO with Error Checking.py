#!/usr/bin/env python3

global message 
message = 'The letter grade is: '

#Function name get_user_grade
def get_user_grade(): 
    grade = (input("What is your numeric grade? "))
    if(grade.isdigit()):
       usergrade = int(grade)
    else:
        usergrade = -1
    return usergrade

#Begin Main program
grade = get_user_grade()

while grade < 0:
    grade = get_user_grade()   

if grade <= 59:
    message = message + 'F, DO NOT give up'
elif grade <= 69:
    message = message + 'D, keep trying'
elif grade <= 79:
    message = message + 'C, Please see your professor '
elif grade <= 89:
    message = message + 'B, great job'
elif grade >= 90:
    message = message + 'A, Congratulations!!! keep the hard work'
print(message)