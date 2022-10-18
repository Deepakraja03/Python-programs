v='aeiou'
c='bcdfghjklmnpqrstvwxyz'
n='0123456789'
vc=cc=nc=0
f=open("f1.txt","r")
a=f.read()
print("The content of the file:",a)
for i in a:
    if i in v:
        vc+=1
    elif i in c:
        cc+=1
    elif i in n:
        nc+=1
print("The number of vowels in the passage:",vc)
print("The number of consonants in the passage:",cc)
print("The number of integers in the passage:",nc)
