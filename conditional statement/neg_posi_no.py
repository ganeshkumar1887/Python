def check_number(num):
    if(num > 0):
        print(f"{num} is positive::")
    elif num == 0:
        print(f"{num} is equal to zero::")
    else:
        print(f"{num} is negative")

n = int(input("Enter a number = "))
check_number(n)
    