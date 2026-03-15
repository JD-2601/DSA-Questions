# check frequency of occurence of each number in an array

arr = list(map(int,input("Entert elements of array:").split()))
frequency = {}
for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num]=1

for key in frequency:
    print(f"{key} occurs {frequency[key]} times")
