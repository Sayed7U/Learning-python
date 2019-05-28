__author__ = 'Sayed'

print("Welcome to the prime number test.")

def is_prime(x):
    if x >= 0:
        if x == 0 or x == 1:
            return False
        elif x == 2:
            return True
        else:
            for n in range(2, x):
                if x % n == 0:
                    return False
                elif n == x - 1:
                    return True
    else:
        return False
number = input("Input an integer: ")

while True:
        if "." in number and not any(c.isalpha() for c in number) or number.isdigit():
            if float(number) - round(float(number)) != 0:
                print("That's not an INTEGER u clapped goat.")
                number = input("Input an integer: ")
            else:
                number = int(number)
                if is_prime(number) is True:
                    print(str(number) + " is a prime number.")
                    number = input("Input an integer: ")
                else:
                    print(str(number) + " is not a prime number.")
                    number = input("Input an integer: ")
        else:
            print("Invalid syntax")
            number = input("Input an integer: ")


