
#the function takes indefinite number of arguments (all must be numbers)
def f1(*args):
    return sum(args) / len(args)

print(f1(2,4,6,8))