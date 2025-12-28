a=[1,2,3,4,5,6]
print("before swaping first and last index",a)
a[0],a[-1]=a[-1],a[0]
print("after swaping first and last index",a)
# 2nd method using temp var..
def swaplist(b):
    size = len(b)
    temp  = b[0]
    b[0] = b[size-1]
    b[size-1]=temp
    return b
b=[1,2,3,4,5,6]
print("before swaping first and last index",b)
print("after swaping first and last index",swaplist(b))