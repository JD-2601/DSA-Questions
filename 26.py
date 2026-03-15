# problem statement 1

def move_hashes(s):
    count = 0
    result = ""

    for ch in s:
        if ch == "#":
            count += 1
        else:
            result += ch

    return "#" * count + result


s = input("Enter the string: ")
print(move_hashes(s))