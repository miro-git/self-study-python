
# Define a function that gets a string and a filepath as parameters and returns the number of occurences of that string in the file.

def foo(character, filepath="bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)

bear_count = foo("bear","files/bear.txt")
print(bear_count)