raw =int(input("Enter no of row::"))
for i in range(1,raw+1):
    print(" " *(raw-i),end=" ") #printing space 

    for j in range(1,2*i):  # printing digit
        print(j,end=" ")
    print()
