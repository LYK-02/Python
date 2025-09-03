# Write a program to fill in a letter template 
# given below with name and date. 

# Letter template
letter = '''Dear Name, 
You are selected! 
Date'''

a =input("enter the name: ")
b =input("enter the date: ")

print(letter.replace("Name", a).replace("Date", b))
