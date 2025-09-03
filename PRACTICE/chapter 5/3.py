#  Create a dictionary of 5 fruits with their colors. Ask the user to enter a 
# fruit name and print its color (if present).]

a ={"orange":"orange",
    "apple":"red",
    "mango":"yellow",}

b = input("enter fruit name :")
c = a.get(b)

if c:
    print("the color is :",c)
else:
    print("sorry fruit color not found")