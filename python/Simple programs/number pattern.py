print("Enter 0 for general number pattern.")
print("Enter 1 for odd number pattern.")
print("Enter 2 for even number pattern.")
a=int(input("Enter the number pattern you desire:"))
if a==0:
    n=int(input("Enter the nth term:"))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=" ")   
        print()
elif a==1:
    n=int(input("Enter the nth term:"))
    for i in range(1,n+1,2):
        for j in range(1,i+1,2):
            print(j, end=" ")   
        print()
elif a==2:
    n=int(input("Enter the nth term:"))
    for i in range(2,n+1,2):
        for j in range(2,i+1,2):
            print(j, end=" ")   
        print()
else:
    print(a, "is not valid.")
