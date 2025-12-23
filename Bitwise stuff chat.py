from time import sleep

def getint(question):
    while True:
        try:
            a = int(input(question))
            return a
        except ValueError as e:
            print (f"{e}\nPlease enter a whole number")

name = input("I'm gonna help you do bitwise stuff but first, what's your name? ")
text = getint(f"{name} enter a number: ")
print ("Your text>>1", text>>1)
