#factorial number
def factorial(a):
    fact=1
    if a==0:
        return 1
    else:
        for i in range(1,a+1):
            fact*=i
        return fact
n = int(input("Enter a number::"))
output = factorial(n)
print("Factorial = ",output)