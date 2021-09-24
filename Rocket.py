print("Welcome to Rocket development system")
print("please enter the details")
print("enter the height of the rocket body ")
a=float(input())
print("enter the weigth of the rocket body")
b=int(input())
print("enter the diameter of the rocket body")
c=float(input())
print("enter the berght of rocket body")
d=int(input())
print("enter the nose of the rocket height")
f=float(input())
print("enter the nose of the rocket  breght")
g=float(input())
print("enter the wing 3 or 4")
h=int(input())
print("enter the type of engine")
print("1.A grade engine - 101s,max weight 30kg ")
print("2.B grade engine - 961s,max weight 20kg ")
print("3.C grade engine - 98s,max weight 15kg ")
j=int(input())
if(a+f <=2 and b<=30 and j==1):
  for i in range (0,100):
    print('|',end='')
  print("Rocket max altitude 1.5km")

elif(a+f <=1.5 and b<=20 and j==2):
  for i in range (0,100):
    print('|',end='')
  print("Rocket max altitude 1.6km")

elif(a+f <=1 and b<=15 and j==2):
  for i in range (0,100):
    print('|',end='')
  print("Rocket max altitude 1.0km")
else:
    print("Something wents wrong in rocket weight or height")
z=a+f
if (z== 2 and b== 20  and j== 1 and h==4):
   print ("Rocket is stable ")
else:
    print("Rocket is unstable")



