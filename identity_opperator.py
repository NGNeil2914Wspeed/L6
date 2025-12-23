from time import sleep
#is is not

def da_thing():
    sleep(1)
    print ("...")
    sleep(1)

def getint(question):
    while True:
        try:
            a = int(input(question))
            return a
        except ValueError as e:
            print (f"{e}\nPlease enter a whole number")

#Introduction
name = input("Hey, i'm gonna use some oppertors and stuff so can u tell me ur name pls? ")

#Part 1 Input
skibidi = getint(f"{name} can u enter a number? ")
hawktuah = getint(f"Now enter the second number: ")
#Part 1 Output
if skibidi is hawktuah:
    a = "is equal to"
else:
    a = "is not equal to"

#Part 2 Input
print (f"Your first number ({skibidi}) {a} your second number ({hawktuah})")
wspeed = input("Now enter smthn: ")
wchat = input("Now enter the second thing: ")

#Part 2 Output
if wspeed is not wchat:
    a = "wchat"
else:
    a = "wspeed"
print (a)