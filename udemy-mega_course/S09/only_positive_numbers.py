def only_positive_numbers(list):
    return [i for i in list if i>0]

positive_only = only_positive_numbers([1,-1,2,-2])

print(positive_only)