# code to find maximum marks from each semester.

n = int(input("Enter number of semesters:"))
for i in range (1,n+1):
    sub = int(input(f"Enter number of subjects in semester {i}:"))

    marks = list(map(int,input(f"Enter marks of subjects in semester {i}:").split()))
    invalid = False

    for m in marks:
        if m<0 or m >100:
            print("invalid marks")
            invalid = True
            break

    if not invalid:
            print(f"Maximum marks in semester{i} is",max(marks))