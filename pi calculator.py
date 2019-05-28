import math
import os
print("Welcome to the python pi calculator")
input("Press enter to start the calculation. ")
n = 1
pi = 0
while n > 0:
    pi = float(pi + (4/n))
    print("pi = " + str(pi))
    n = n+2
    pi = float(pi - (4/n))
    print("pi = " + str(pi))
    n = n+2
