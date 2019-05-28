__author__ = 'Sayed'
print "Welcome to odd or even number tester."
number = int(raw_input("Type in number to test: "))

while True:
    if number % 2 == 0:
        print "Number is even."
        number = int(raw_input("Type in number to test: "))
    else:
        print "Number is odd."
        number = int(raw_input("Type in number to test: "))