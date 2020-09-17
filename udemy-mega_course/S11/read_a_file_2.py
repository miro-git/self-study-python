with open("files/fruits.txt") as myfile:
    content = myfile.read()
    # the file will be atomatically closed
print(content)