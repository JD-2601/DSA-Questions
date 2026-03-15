# traverse elements of a matrix in spiral order.

matrix = []

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

# input matrix
for i in range(r):
    row = list(map(int, input(f"Enter elements for row {i+1}: ").split()))
    matrix.append(row)

top = 0
bottom = r - 1
left = 0
right = c - 1

print("Spiral order:")

while top <= bottom and left <= right:

    # move right
    for i in range(left, right + 1):
        print(matrix[top][i], end=" ")
    top += 1

    # move down
    for i in range(top, bottom + 1):
        print(matrix[i][right], end=" ")
    right -= 1

    # move left
    if top <= bottom:
        for i in range(right, left - 1, -1):
            print(matrix[bottom][i], end=" ")
        bottom -= 1

    # move up
    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(matrix[i][left], end=" ")
        left += 1