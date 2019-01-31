#!/usr/bin/env python3

####################################################################
# Factorial function
# For any number, N, its factorial is (N)x(N-1)x(N-2)x . . . x (1)
# Example:  3! = 3x2x1 = 6
# Example:  4! = 4x3x2x1 = 24
# Example:  5! = 5x4x3x2x1 = 120
####################################################################

# Query the user for the number
print("This program computes the factorial for a given number. . .")
x = int(input("Enter a number: "))

# Initial value of the factorial
factorial = 1

####################################################################
# The range function (start, stop) does not include the stop value
# Hence you want to make the stop value, x+ 1 (instead of x)
####################################################################
for i in range(1, x+1):
    factorial = factorial * i

# Print out the computed value of the factorial
print(x, '! = ', factorial)