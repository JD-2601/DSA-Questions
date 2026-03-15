# Find middle node
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

mid = n // 2

print(arr[mid:])