# multiplication table
def printTable(num):
    
    if num==0:
        return 0
    else:
        for i in range(1,11):
            print(f"{num} * {i} = {num * i}")
n = int(input("Enter a number::"))
table=printTable(n)