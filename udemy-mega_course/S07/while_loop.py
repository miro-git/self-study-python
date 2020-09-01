
myinput =''

while True:
    myinput = input("What is your name?")
    if myinput == 'pypy':
        break
    else:
        continue

print ("Thanks " + myinput)