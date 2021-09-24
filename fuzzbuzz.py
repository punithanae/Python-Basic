n= int(input())
for i in range(0,n+1):
    if(i%3==0 and i%5==0):
        print("FuzzBuzz")
    elif(i%3==0 and i%5!=0):
        print("Fuzz")
    elif(i%3!=0 and i%5==0):
        print("Buzz")
    else:
        print(i)
