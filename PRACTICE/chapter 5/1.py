# . Create a dictionary to store names of 3 students as keys and their marks as
# values. Print the student with the highest marks

a = {"aamir" : 81. ,
     "arfat" : 20,
     "ammar" : 81.098765 }

b = max(a, key=a.get)
c = min(a, key=a.get)

print("student with highest marks is " ,b, "with" ,a[b] , "marks" )
print("student with lowest marks is " ,c, "with" ,a[c] , "marks" )