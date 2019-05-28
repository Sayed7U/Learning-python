__author__ = 'Sayed'
print("Welcome to the day finder. Using Zellers algorithm")
d = int(input("Enter a date (1-31)"))
m = int(input("Enter a month (1-12) "))
y = int(input("Enter a year (YYYY)"))

days = ["Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday"]


def zellers(d, m, y):
    if m < 3:
        m += 12
        y -= 1
    c = y // 100
    ypri = y - (c*100)
    sumval = int(2.6*m - 5.39) + int(ypri/4) + int(c/4) + d + ypri - 2*c
    return sumval % 7

while True:
    output = zellers(d, m, y)
    for i in range(0,7):
        if output == i:
            print(str(d) + "/" + str(m) + "/" + str(y) + " was a " + days[i])
    d = int(input("Enter the date (1-31)"))
    m = int(input("Enter the month (1-12) "))
    y = int(input("Enter the year (YYYY)"))
