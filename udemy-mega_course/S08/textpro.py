total_input = ""
question_starters = ("how","why","who","where")

while True:
    myinput = input("Say smt: ")
    addquestionmark = False
    if myinput == "-end":
        total_input 
        print("Here is all you said so far: ")
        print(total_input)
        break
    else:
        myinput = myinput.strip()    #removes any whitespace from the beginning or the end
        mysplitinput = myinput.split(" ") #splits the string into substrings if it finds instances of the separator 
        for word in question_starters:
            if mysplitinput[0]==word:
                addquestionmark = True
        
        if addquestionmark:
            if myinput[-1] != "?":
                myinput = myinput + "? "
        else:
            if myinput[-1] != ".":
                myinput = myinput + ". "  
                  
        myinput = myinput.capitalize()
        total_input = total_input + myinput
        continue
