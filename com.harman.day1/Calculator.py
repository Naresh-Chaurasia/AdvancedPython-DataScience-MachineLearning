def addition_no_args():
    s = 10+20
    return s

def addition_args(x, y):
    s = x + y
    return s

def addition_no_return(x, y):
    s = x + y
    print(s)

print(addition_no_args())
print(addition_args(100,200))
print(addition_no_return(1,2))