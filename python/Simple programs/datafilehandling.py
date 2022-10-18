f=open("f1.txt","r")
s=f.readlines()
print('\n')
for i in s:
    a=i.replace(" ","#")
    print(a)
f.close()
