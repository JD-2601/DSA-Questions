# rotate a matrix clockwise by 90 degrees.

n = int(input("Enter size of matrix:"))
matrix = []

for i in range(n):
    row = list(map(int,input(f"Enter row {i+1} elements: ").split()))
    matrix.append(row)

print("Rotated matrix:")

for i in range(n):
    for j in range(n-1,-1,-1):
        print(matrix[j][i],end="   ")
    print()