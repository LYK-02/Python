# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

a = input("enter the sentence ").lower()

if ((p1.lower() in a) or (p2.lower() in a) or(p3.lower() in a) or(p4.lower() in a)):
    print("this comment is spam")
else:
    print("this comment is not a spam")