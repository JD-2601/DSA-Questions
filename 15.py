# Reverse an array.

arr = []
n = int(input("Enter the number of elements: "))
for i in range (n):
    elem = int(input(f"Enter element {i+1}: "))
    arr.append(elem)
rev_arr = arr[::-1]
print("Reversed array : ", rev_arr)