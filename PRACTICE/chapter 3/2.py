#  Ask the user to input a sentence and count 
# the number of vowels in it.

a = input("enter thee sentence :")
b = "aeiouAEIOU"
count = 0

for ch in a:
    if ch in b:
     count = count + 1

print("the total no of vowel is :",count)