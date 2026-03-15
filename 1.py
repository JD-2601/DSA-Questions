# Write a function to check whether a given input number is prime or not.

#step 3
def is_prime(n):
    if n<1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

#step 1
num = int(input("Enter a number:"))

#step 2(calling function) & step 4(printing result)
if is_prime(num):
    print(num,"is a prime number.")
else:
    print(num,"is not a prime number.")
