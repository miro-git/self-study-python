# myfile = open("fruits.txt")
# content = myfile.read()
# myfile.close()
# print(content)

with open("fruits.txt") as myfile:
    content = myfile.read()

print(content)