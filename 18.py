# 

n = int(input("Enter number of elements in array : "))
arr1 = []
for i in range(n):
    elem = int(input(f"Enter element {i+1} : "))
    arr1.append(elem)
arr2 = []

for j in arr1:
    if j not in arr2:
        arr2.append(j)
    else:
        print(j," is duplicate element.")
