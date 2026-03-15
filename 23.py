# Move zeroes to end

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    elem = int(input(f"Enter element {i+1}: "))
    arr.append(elem)

pos = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1

print("Array after moving zeros:", arr)