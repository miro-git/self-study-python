def int_list(list):
    return [i if isinstance(i, int) else 0 for i in list] 
    
print(int_list(["a",1,"b",2,"c",3]))