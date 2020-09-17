with open("files/bear.txt") as file:
    content = file.read()

with open("files/bear_first_90.txt", "w") as file:
    file.write(content[:90])