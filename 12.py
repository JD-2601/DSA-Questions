# Find the second smallest and second largest element in an array.

arr = list(map(int,input("Enter the elements of array:").split()))
arr = list(set(arr))
arr.sort()


if len(arr) <2:
    print('-1')

else :
    second_smallest = arr[1]
    second_largest = arr[-2]
    print("Second smallest element is: ",second_smallest)
    print("Second largest element is: ",second_largest)