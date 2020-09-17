def copy_n_times(filepath,repetitions):
    with open(filepath,"r") as getdata:
        content = getdata.read()
        # print(content)
        
    for i in range(repetitions):
        with open(filepath,"a+") as mytext:
            mytext.write("\n")
            mytext.write(content)


copy_n_times("files/data.txt",3)

