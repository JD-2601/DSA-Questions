# First unique character in a string.
s = input("Enter the string: ")

for i in range(len(s)):
    if s.count(s[i]) == 1:
        print("Index:", i)
        break
else:
    print(-1)