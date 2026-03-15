# counting values

n = int(input("Enter number of steps: "))
path = input("Enter path: ")

level = 0
valleys = 0

for step in path:
    if step == "U":
        level += 1
        if level == 0:
            valleys += 1
    else:
        level -= 1

print("Number of valleys:", valleys)