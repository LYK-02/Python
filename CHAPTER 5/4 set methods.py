# • len(s): Returns 4, the length of the set  
# • s.remove(8): Updates the set s and removes 8 from s. 
# • s.pop(): Removes an arbitrary element from the set and return the element 
# removed. 
# • s.clear():empties the set s. 
# • s.union({8,11}): Returns a new set with all items from both sets. {1,8,2,3,11}. 
# • s.intersection({8,11}): Return a set which contains only item in both sets  {8}.

s = {1, 5, 32, 54,5, 5, 5, "Harry"}

print(s, type(s))

s.add(566)
print(s, type(s))
s.remove(1)
print(s, type(s))