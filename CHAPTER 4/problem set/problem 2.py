# Write a program to accept marks of 6 students and display 
# them in a sorted manner. 

a = []

f1 = int(input("enter the marks here:"))
a.append(f1)
f2 = int(input("enter the marks here:"))
a.append(f2)
f3 = int(input("enter the marks here:"))
a.append(f3)
f4 = int(input("enter the marks here:"))
a.append(f4)
f5 = int(input("enter the marks here:"))
a.append(f5)
f6 = int(input("enter the marks here:"))
a.append(f6)

a.sort()


print("marks are:", a)