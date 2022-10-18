import random
t='CBSEONLINE'
count=random.randint(0,3)
c=9
while t[c]!='L':
    print(t[c]+t[count]+"*",end="")
    count=count+1
    c=c-1
  
