# Merge two sortd linked lists
list1 = list(map(int, input("Enter elements of list1: ").split()))
list2 = list(map(int, input("Enter elements of list2: ").split()))

merged = sorted(list1 + list2)

print(merged)