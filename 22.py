# count pairs with target value
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    elem = int(input(f"Enter element {i+1}: "))
    arr.append(elem)

k = int(input("Enter target sum: "))

count = 0

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == k:
            count += 1

print("Number of pairs:", count)