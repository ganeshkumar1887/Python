def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def main():
    print("---Simple Calculator---")
    n1 = int(input("Enter 1st number::"))
    n2 = int(input("Enter 2nd number::"))
    print("Addition = ",add(n1,n2))
    print("subtraction = ",sub(n1,n2))
    print("Multiplication = ",mul(n1,n2))
    print("Division = ",div(n1,n2))
if __name__ =="__main__":
    main()
