s=input("ente a sentence:")
d=0
f=0
for c in s:
    print(c)
    if c.isupper():
        d=d+1
    else:
        f=f+1
print("upper",d)
print("lower",f)
