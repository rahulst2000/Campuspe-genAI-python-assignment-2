# This program checks a given string is a palindrome.
# The user enters a string.
# The program compares the string with its reverse.
# It prints whether the string is a palindrome or not.

s = input("Enter string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")