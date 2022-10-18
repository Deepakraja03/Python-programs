uc=0
lc=0
f=open("f1.txt")
a=f.read()
for i in a:
    if i in ['a','e','i','o','u']:
        lc+=1
    elif i in ['A','E','I','O','U']:
        uc+=1
print("Number of uppercase vowels:", uc)
print("Number of lowercase vowels:", lc)
f.close()
