# find  an element"s indexing  using binary search.

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] <key:
            low = mid+1
        else:
            high = mid-1
    return -1

# input
arr = list(map(int,input("Enter elements of sorted array:").split()))
key = int(input("Enetr element to search:"))
result = binary_search(arr,key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")