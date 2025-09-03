#  14. Check if a given string is a palindrome (e.g., 'madam', 'racecar')

a = input("enter the palindrome :")  # take user input
b = a[::-1]    # new concept      # reverse the string

print(a == b)  # check if original == reversed


