# Reverse a linked list.
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

prev = None
curr = 0

while curr < n:
    prev, arr[curr] = arr[curr], prev
    curr += 1

print(arr[::-1])