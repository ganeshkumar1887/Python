year=int(input("Enter the year = "))
if(year%4==0 and year%100!=0)or(year % 4 ==0):
    print(f"{year} is leap year::")
else:
    print(f"{year} is non leap year::")