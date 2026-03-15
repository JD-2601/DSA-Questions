# Palindrome string.
s = input("Enter string: ")

if s == s[::-1]:
    print("true")
else:
    print("false")