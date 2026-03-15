# Reverse a string
s = input("Enter the string: ")

rev = ""

for i in range(len(s)-1, -1, -1):
    rev += s[i]

print("Reversed string:", rev)