# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

s={}

a = input("enter friend name :")
b = input("enter language :")
s.update({a : b})
a = input("enter friend name :")
b = input("enter language :")
s.update({a : b})
a = input("enter friend name :")
b = input("enter language :")
s.update({a : b})
a = input("enter friend name :")
b = input("enter language :")
s.update({a : b})

print(s)
