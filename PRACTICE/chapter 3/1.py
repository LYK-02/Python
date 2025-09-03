# Write a program that takes a user’s full name as input and prints 
# only the initials (e.g., 'Harry Potter' → 'H.P.')\

a = input("enter the full name:")
b = a.split()
c = ""

for word in b :
    c = c + word[0].upper() + "."
 

print(c)
