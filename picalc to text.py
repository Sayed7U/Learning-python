import math
import os
from decimal import *
getcontext().prec = 70
print("Welcome to the python pi calculator v2")
print(0.75)
print(4/3)
count_max = int(input("Number of counts for calculation: "))
x = Decimal(2)
y = Decimal(3)
z = Decimal(4)
pi = Decimal(3)
file = open("C:\\Users\\Sayed\\Documents\\python\\pidigits.txt","w")
count = 0

while count <= count_max:
    pi = Decimal(pi + (4/(x*y*z)))
    x += 2
    y += 2
    z += 2
    pi = Decimal(pi - (4/(x*y*z)))
    x += 2
    y += 2
    z += 2
    count += 1
file.write(str(pi))
print(pi)
file.close()
