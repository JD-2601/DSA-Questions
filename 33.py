# Find the first Non- repeated character in a string.
s = input("Enter string: ")

for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break