#  Make a set of numbers {1,2,3,4,5} and demonstrate union, intersection, and 
# difference with another set {4,5,6,7}.

a = {1,2,3,4,5}
b = {4,5,6,7}

c = a.union(b)   # or a | b
d = a.intersection(b)   # a & b
e = a.difference(b)   # a - bf
f = b.difference(a)   # b - a\

print("the union of a and b is",c)
print("the intersection of a and b is",d)
print("the difference of a-b is",e)
print("the difference of b-a is",f)