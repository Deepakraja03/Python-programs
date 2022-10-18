import mysql.connector as m
mycon=m.connect(host='localhost',user='root',passwd='deepak',database='as')
print(mycon.is_connected())
cur=mycon.cursor()
class Upload_Details:
    def __init__ (self,name,age,location,B_group,quantity,Gender,mobile):
        self.name=name
        self.age=age
        self.location=location
        self.B_group=B_group
        self.quantity=quantity
        self.Gender=Gender
        self.mobile=mobile
name=str(input("Enter name of the donar:"))
age=int(input("Enter age:"))
location=str(input("Enter location:"))
B_group=str(input("Enter Blood Group:"))
quantity=int(input("Enter quantity of the Blood:"))
Gender=str(input("Male or Female:"))
mobile=int(input("Enter mobile number:"))
UD=Upload_Details(name,age,location,B_group,quantity,Gender,mobile)
val = (name,age,location,B_group,quantity,Gender,mobile)
cur.execute("INSERT INTO bd (name,age,location,bgroup,qnt,gender,pno) VALUES (%s, %d,%s,%s,%d,%s,%d)",val)
cur.commit()
cur.execute('select * from bd')
for i in cur:
    print(i)