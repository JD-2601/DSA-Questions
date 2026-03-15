# Intersection of two arrays

n1 = int(input("Enter number of elements in first array: "))
arr1 = []

for i in range(n1):
    elem = int(input(f"Enter element {i+1}: "))
    arr1.append(elem)

n2 = int(input("Enter number of elements in second array: "))
arr2 = []

for i in range(n2):
    elem = int(input(f"Enter element {i+1}: "))
    arr2.append(elem)

intersection = []

for i in range(len(arr1)):
    if arr1[i] in arr2 and arr1[i] not in intersection:
        intersection.append(arr1[i])

print("Intersection of arrays:", intersection)