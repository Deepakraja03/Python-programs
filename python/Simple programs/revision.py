a=input("Enter the text to be reversed:")
b=list(a)
l=len(b)
for i in range(0,l):
    c=b.pop()
    print(c, end='')

