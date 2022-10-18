m=int(input("Enter the mark:"))
if m>90 and m<=100:
    print("You have got A.")
elif m>80 and m<90:
    print("You have got B.")
elif m>70 and m<80:
    print("You have got C.")
elif m>60 and m<70:
    print("You have got D.")
elif m<=60:
    print("You have got E.")
else:
    print("The entered mark is more than 100.")

