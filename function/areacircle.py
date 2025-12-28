# Area of circle 
def areaCircle(rds):
    area = 3.14*rds*rds
    print("Area of circle:",area)
def perimeter(rd):
    per = 2 * 3.14 * rd
    print("Perimeter of circle = ",per)

print("Welwcome ! find Area of circle and perimeter-->")
r = int(input("Enter a radius ::"))
areaCircle(r)
perimeter(r)
