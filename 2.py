# code to generate all pythagorean triplets with values under a certain limit

limit = int(input("Enter a value for limit:"))

for a in range(1,limit):
    for b in range(a+1,limit):
        for c in range(b+1,limit):
            if a**2 + b**2 == c**2:
                print(a,b,c)