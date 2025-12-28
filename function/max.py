# maximum in n number
def findmax(a,b,c):
    return(max(a,b,c))

n1=int(input("Enter 1st number::"))
n2=int(input("Enter 2nd number::"))
n3=int(input("Enter 3rd number::"))
maxNum=findmax(n1,n2,n3)
print("Maximum number = ",maxNum)