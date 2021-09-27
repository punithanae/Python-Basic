def fact(x):
    if x==0 or x==1:
        return 1
    return  x *fact(x-1)
x=int(input())
print(fact(x))
