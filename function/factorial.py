def fact(num):
    factorial = 1
    while num>=1:
        factorial = factorial * num
        num = num -1
    return factorial
n = int(input("Enter a number::"))
for i in range(1,n):
    print("factoirial of ",i,"is :",fact(i))