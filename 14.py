# matrices are identical?

r= int (input("Enter number of rows : "))
c= int (input("Enter number of columns : "))    

A = []
B = []

for i in range(r):
    row = list(map(int,input(f"Enter row{i+1} elements for matrix A: ").split()))
    A.append(row)

for i in range(r):
    row = list(map(int,input(f"Enter row {i+1} elements for matrix B: ").split()))
    B.append(row)

if A == B:
    print("The matrices are identical.")
else:   
    print("The matrices are not identical.")