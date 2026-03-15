# Check valid arguments
s = input("Enter first string: ")
t = input("Enter second string: ")

if sorted(s) == sorted(t):
    print("True")
else:
    print("False")