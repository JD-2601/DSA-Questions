# Merge interval

n = int(input("Enter number of intervals:"))
intervals = []

for i in range(n):
    start, end = map(int,input(f"Enter interval {i+1} (start end):").split())
    intervals.append([start, end])

    intervals.sort()

    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[0])

print("Merged intervals:")
for i in merged :
    print(i)
