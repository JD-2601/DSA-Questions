
n = int(input("Enter the number of elements: "))
arr=[]
for i in range(n):
    elem = int(input(f"Enter integer {i+1}: "))
    arr.append(elem)
max_subarray_prod = 0

for j in range (len(arr)):
    for k in range(j+1,len(arr)):
        prod = arr[j]*arr[k]
        if prod > max_subarray_prod:
            max_subarray_prod = prod
            max_subarray_indices = (j, k)
print("Subarray for maximum product is : (",max_subarray_indices[0],",",max_subarray_indices[1],")")
print("Maximum product of subarray is : ", max_subarray_prod)


