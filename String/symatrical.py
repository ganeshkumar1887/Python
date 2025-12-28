def palindrom(st):
    return st == st[::-1]
def symmetrical(st):
    length = len(st)
    mid = length//2
    if length % 2 == 0:
        return st[:mid]==st[mid:]
    else :
        return st[:mid]==st[mid+1:]
    
st =  input("Enter the String = ")
if symmetrical(st):
    print("Given string is symmetrical")
else:
    print("Given string is not symmetrical")
if palindrom(st):
    print("Given string is palindrom")
else:
    print("Given string is not palindrom")
