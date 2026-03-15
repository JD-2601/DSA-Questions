# Longest substring without repeating characters
s = input("Enter string: ")

longest = 0

for i in range(len(s)):
    seen = ""
    for j in range(i, len(s)):
        if s[j] not in seen:
            seen += s[j]
            longest = max(longest, len(seen))
        else:
            break

print(longest)