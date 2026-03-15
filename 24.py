# Majority elemengt

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    elem = int(input(f"Enter element {i+1}: "))
    arr.append(elem)

majority = None

for i in range(len(arr)):
    count = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    if count > n//2:
        majority = arr[i]
        break

print("Majority element:", majority)