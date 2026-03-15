# Merge two arrays and sort the merged array.

m = int(input("Enter number of elements in nums1: "))
nums1 = list(map(int, input("Enter elements of nums1: ").split()))

n = int(input("Enter number of elements in nums2: "))
nums2 = list(map(int, input("Enter elements of nums2: ").split()))

nums1 = nums1[:m]   # keep only first m elements

for num in nums2:
    nums1.append(num)

nums1.sort()

print("Merged array:", nums1)