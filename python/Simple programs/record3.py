v=['a','e','i','o','u','A','E','I','O','U']
vc=0
c=0
u=0
l=0
f=open("f1.txt","r")
r=f.read()
print(r)
f.seek(0)
while True:
    a=f.readline()
    if not a:
        break
    for i in a:
        if i in v:
            vc+=1
        else:
            c+=1
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
print("Total number of vowels",vc)
print("Total number of consonants",c)
print("Total number of upper case",u)
print("Total number of lower case",l)
f.close()
