# Take 5 integers as input from the user, store them in a list, and 
# print the maximum and minimum values.

a = []

n = int(input("enter the no:"))
a.append(n) 
n = int(input("enter the no:"))
a.append(n) 
n = int(input("enter the no:"))
a.append(n) 
n = int(input("enter the no:"))
a.append(n) 
n = int(input("enter the no:"))
a.append(n) 

print("the number are :",a)
print("the maximum no :",max(a))
print("the minimum no :",min(a))
