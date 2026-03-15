# string rotation check
s = input("Enter first string: ")
goal = input("Enter goal string: ")

if len(s) == len(goal) and goal in (s + s):
    print("true")
else:
    print("false")