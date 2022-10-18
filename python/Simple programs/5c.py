n=int(input("Enter the last term:"))
f=0
s=1
print(f)
print(s)
for i in range(1,n+1):
    t=f+s
    print(t)
    f,s=s,t
