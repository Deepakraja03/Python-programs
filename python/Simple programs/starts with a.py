c=0
f=open("f1.txt","r")
r=f.read()
print("The given file is", r,'\n')
f.seek(0)
while True:
    a=f.readline()
    if not a:
        break
    if a[0]=='a' or a[0]=="A":
        print(a)
        c+=1
print("Total number of lines starting with a or A is", c)
f.close()
