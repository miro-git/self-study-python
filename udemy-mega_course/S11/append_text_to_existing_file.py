with open("files/vegetables.txt","a+") as mytext:
    mytext.write("\nEggplant")
    # move the cusros to the begining of the file
    mytext.seek(0) 
    content = mytext.read()

print(content)