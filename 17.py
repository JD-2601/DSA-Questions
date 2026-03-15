# Missing Number

n = int(input("Enter the number of elements: "))
arr = []
for i in range (n):
    elem = int(input(f"Enter element {i+1} : "))
    arr.append(elem)

arr.sort()
#first_elem
a = arr[0]
#last_elem 
b = arr[-1]

for j in range(a,b):
    if j not in arr:
        print("Missing number is : ",j)