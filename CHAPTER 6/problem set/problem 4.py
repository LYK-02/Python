# Write a program to find whether a given username contains less than 10 
# characters or not. 

a = input("enter the username:")

if (len(a)<10):
    print("Your username contains less than 10 characters")
else:
     print("Your username contains more than or equal to 10 characters")