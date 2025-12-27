from time import sleep

def da_thing():
    sleep(1)
    print ("...")
    sleep(1)

name = input("Im gonna help u find the ascii value of stuff but first, whts ur name? ")
running = True
while running:
    pra = input(f"Hey {name}, please enter something")
    if len(pra) > 1 or len(pra) == 0:
        print ("Please enter only 1 character")
        da_thing
    else:
        dgjk = ord(pra)
        running = False
print ("The ascii value is", dgjk)
