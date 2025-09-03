# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.

m1 =int(input("enter the maks :"))
m2 =int(input("enter the maks :"))
m3 =int(input("enter the maks :"))

percentage = (m1 + m2 + m3)/3

if(percentage>= 40 and m1 >= 33 and m2 >= 33 and m3 >= 33 ):
    print("you are pass.\npercente is :",percentage)
else :
    print("better luck next time\npercente is :",percentage)