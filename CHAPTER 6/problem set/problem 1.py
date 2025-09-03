# Write a program to find the greatest of four numbers entered by the user.

a = int(input("enter the no :"))
b = int(input("enter the no :"))
c = int(input("enter the no :"))
d = int(input("enter the no :"))

if (a>b and a>c and a>d):
    print("the greatest no is a :",a)
elif (a<b and b>c and b>d):
    print("the greatest no is b :",b)
elif (a<c and c>b and c>d):
    print("the greatest no is c :",c)
elif (d>b and d>c and d>a ):
    print("the greatest no is d :",d)