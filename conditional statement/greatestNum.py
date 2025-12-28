a=int(input("Enter 1st Number::"))#5
b=int(input("Enter 2nd Number::"))#9
c=int(input("Enter 3rd Number::"))#7
if(a>=b and a>=c):         #5>=9 not 5>=7 not
    print("1st number is greatest Number",a) 
elif(b>=a and b>=c):        #9>=5 yes 9>=7 yes
    print("2nd number is greatest Number",b)
else:                       #7>=5 not 7>=5 yes 
    print("3rd number is greatest Number",c)
