file = open("files/bear.txt")
content = file.read()
file.close()
# print out the first 90 characters of its content
print(content[:90])