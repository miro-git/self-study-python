import json
data = json.load(open("files/data.json"))

# import difflib
from difflib import get_close_matches

print("The type of 'data' is: ")
print(type(data))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]  
    elif w.upper() in data:
        return data[w.upper()]               
    elif len(get_close_matches(w,data.keys(),cutoff=0.8))>0:
        yes_or_no = False
        while yes_or_no == False:
            yn = input("Did you mean '%s' instead? Enter Y or N: " % get_close_matches(w, data.keys(),cutoff=0.8)[0])
            yn = yn.lower()
            if yn == "y":   
                yes_or_no = True
                return data[get_close_matches(w,data.keys(),cutoff=0.8)[0]]
            elif  yn == "n":
                yes_or_no = True
                return "The word '%s' does not exist in our dictionary." % w       
    else:
        return "The word '%s' does not exist in our dictionary." % w

while True:
    word = input("Enter a word: ")

    output = translate(word)

    if type(output) == list:
        for i in output:
            print(i)
    else:
        print(output)        



