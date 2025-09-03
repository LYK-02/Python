# Write a program which finds out whether a given name is present in a list or not.

a =  ["abbas","aamir","ammar","laik"]

b = input("enter the name:").lower()

if (b in a):
    print("your name is in the list")
else:
    print("your name is not in list")