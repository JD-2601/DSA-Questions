# Kth largest element.

n = int(input("Enter number of elements for array: "))
arr = []
for i in range(n):
    elem = int(input(f"Enter element {i+1}: "))
    arr.append(elem)

K = int (input("Enter the value of K: "))
arr.sort()
Kth_element = arr[-K]
print("Kth largest element is : ",Kth_element)