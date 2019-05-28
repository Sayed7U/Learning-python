__author__ = 'Sayed'
for i in range(10):
    print i**2
else:
    x = 12
    while x < 20:
        print x**3
        x += 1
        if x**3 > 5000000:
            break
    else:
        raw_input(".")
