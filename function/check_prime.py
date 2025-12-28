def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            return False
    return True
def main():
    n = int(input("Enter a number::"))
    if is_prime(n):
        print(f"{n} is prime number::")
    else:
        print(f"{n} is not prime number::")
main()