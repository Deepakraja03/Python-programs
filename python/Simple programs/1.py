f=open("f1.txt","r")
str=""
while str:
    str=f.readline()
    print(str , end="#")
f.close()
