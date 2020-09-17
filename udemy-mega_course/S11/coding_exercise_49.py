# Append the text of bear1.txt to bear2.txt. In other words, bear2.txt should contain its text and the text of bear1.txt after that.

with open("files/bear1.txt","r") as bear1txt:
    content1 = bear1txt.read()
    print("-- bear 1 --")
    print(content1)

with open("files/bear2.txt","a+") as bear2txt:
    bear2txt.write("\n")
    bear2txt.write(content1)
    bear2txt.seek(0)
    content2 = bear2txt.read()  
    print("-- bear 2+1 --")
    print(content2)