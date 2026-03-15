# solve an equation and take 3 inputs.

def solve_equation(a,b):
    result = a**3 + 3*(a**2)*b + 3*a*(b**2) + b**3
    return result
a = int(input("Enter a value for a :"))
b = int(input("Enter a value for b :"))
c = int(input("Enter a value for c :"))

answer = solve_equation(a,b)
print("Result = ",answer)