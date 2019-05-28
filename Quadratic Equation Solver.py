import math
import os
from sys import exit
print("Welcome to the Quadratic Equation solver -- by Zarfots/Zarfeet")
def prints():
    print("ax^2 + bx + c = 0")
    print("Please give the values of a, b and c to work out equation.")

solve1 = 0
prints()
def checkIntValue(Inputs):
    while True:
        try:
            val = float(Inputs)
            return
        except ValueError:
            print("Input must be an integer and greater than 0.")
            exit("Error message")
            return
def Anotherq():
    Another = input("Solve Another?(Y/N): ")
    Yes = {"Y", "Yes", "yes", "YES", "y"}
    No = {"N", "No", "no", "NO", "n"}
    if Another in Yes:
        print("\n")
        prints()
        abcInputs()
    elif Another in No:
        print("Goodbye.")
        exit()
    else:
        print("Invalid syntax.")
        exit()
def SolveQuadratic(a, b, c):
    print("--------------------")
    print(str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0")
    a = float(a)
    b = float(b)
    c = float(c)
    x = (b**2)-(4*a*c)
    root = math.sqrt(x)
    top = -b + root
    topm = -b - root
    answer = top/(2*a)
    answer2 = topm/(2*a)
    print("x = %.2f" % answer + "(2 D.P)")
    print("x = %.2f" % answer2 + "(2 D.P)")
    Anotherq()
    return
def abcInputs():
    aInput = input("Value for a(>0): ")
    checkIntValue(aInput)

    bInput = input("Value for b: ")
    checkIntValue(bInput)
    
    cInput = input("Value for c: ")
    checkIntValue(cInput)
    aInput = float(aInput)
    bInput = float(bInput)
    cInput = float(cInput)
    if bInput**2-(4*aInput*cInput) < 0:
        print("This equation does not have real roots.")
        os.system("pause")
    else:
        SolveQuadratic(aInput, bInput, cInput)
        return
if solve1 == 0:
    abcInputs()
    solve1 = 1

