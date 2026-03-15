# calculate tyres for both cars and bikes in dealerships.

n = int(input("Enter number of dealerships:"))

for i in range(n):
    cars, bikes = map(int,input(f"Enter number of cars and bikes respectively in dealership {i+1}:").split())
    tyres = (cars*4) + (bikes*2)
    print(f"Total number of tyres in dealership {i} is {tyres}")