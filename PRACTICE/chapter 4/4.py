#  Write a program to merge two lists and remove duplicate values.

a = (1,23,4,5,6,7,8)
b = (1,2,3,45,6,7,8)
c = a + b
d = set(c)

e = list(d)  # agar list chaiye toh ye use hoga

print(d)