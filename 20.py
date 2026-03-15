# roate array by k times from right.
n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    elem = int(input(f"Enter element {i+1}: "))
    arr.append(elem)

k = int(input("Enter number of rotations: "))

k = k % n

rotated = arr[-k:] + arr[:-k]

print("Rotated array:", rotated)