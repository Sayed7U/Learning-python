__author__ = 'Sayed'
def reverse(text):
    newtext = ""
    for i in range(len(text) - 1, -1, -1):
        newtext+=str(text[i])
    return newtext
x = raw_input("enter_text: ")
while True:
    print reverse(x)
    x = raw_input("enter_text: ")
