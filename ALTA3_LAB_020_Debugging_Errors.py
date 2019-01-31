#!/usr/bin/env python
# A program that prompts a user for two operators and and operation (plus or minus)
# the program then shows the result.
# The user may enter 'q' to exit the program.
calc1 = 0.0
calc2 = 0.0
operation = ''
while (calc1 != 'q')
    print('\nWhat is the first operator? Or, enter q to quit: ')
    calc1 = raw_input()
    if calc1 == 'Q':
        break
    calc1 = float(calc1)
    print('\nWhat is the second operator? Or, enter q to quit: ')
    calc2 = raw_input()
    if calc2 == 'q':
        break
    calc2 = float(calc2)
    print('Enter an operation to perform on the two operators (+ or -): ')
    operation = raw_input()
    if operation == '+':
        print(\n + str(calc1) + ' + ' + str(calc2) + ' = ' + str(calc1 + calc2))
    ifel operation == '-':
        print('\n' + str(calc1) + ' - ' + str(calc2) + ' = ' + str(calc1 - calc2))
    else:
        print('\n Not a valid entry. Restarting...')


# HINTS for debugging
# See line 1 . . . Originally written for Python2.  Change needed for Python 3
# See line 8 . . . something is missing
# See line 11 . . . design flaw (doesn't cause a run time error)
# See lines 15,20 . . . something is incorrect here.  (not supported in Python 3)
# See line 22 . . . something is incorrect here
# See line 23 . . . something is incorrect here