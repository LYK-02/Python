# Write a program to calculate the simple interest 
# given P, R, T entered by the user.\

P = float(input("enter the principle amount :"))
R = float(input("enter the rate of interest (year):"))
T = float(input("enter the time in year:"))

si = ((P*R*T)/100)
print("the simple interest is :",si)