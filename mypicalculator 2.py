import math
import os
from decimal import *
getcontext().prec = 70
print("Welcome to the python pi calculator v2")
print(0.75)
print(4/3)
input("Press enter to start the calculation. ")
x = Decimal(2)
y = Decimal(3)
z = Decimal(4)
pi = Decimal(3)

while pi > 0:
    pi = Decimal(pi + (4/(x*y*z)))
    print ("pi = " + str(pi))
    x += 2
    y += 2
    z += 2
    pi = Decimal(pi - (4/(x*y*z)))
    print ("pi = " + str(pi))
    x += 2
    y += 2
    z += 2
