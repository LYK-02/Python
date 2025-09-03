# Write a program to check whether the key 'Python' exists in a given dictionary

a ={"python":"1",
    "java": "2",
    "c++": "3"}

b = input("enter the number :")

if b in a :
    print("Key exists:", b, "with value", a[b])
else:
    print("Key not found")
