n=int(input("Enter the number of numbers:"))
e=0
o=0
for i in range(1,n+1):
    a=int(input("Enter the number:"))
    if a%2==0:
        e=e+a
    else:
        o=o+a
print("The sum of even numbers is", e)
print("The sum of odd numbers is", o)
