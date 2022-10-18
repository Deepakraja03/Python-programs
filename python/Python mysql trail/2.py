import mysql.connector as m
mycon=m.connect(host='localhost',user='root',passwd='2029',database='college')
print(mycon.is_connected())
cur=mycon.cursor()
cur.execute('drop table student')
cur.execute('''create table student(RollNo integer primary key,Name varchar(30) not null,Course varchar(30),Phone_Number char(10),EmailID varchar(35),Fee varchar(10))''')
cur.execute('desc student')
ans='y'
while ans.upper()=='Y':
    r=int(input("Enter the roll number:"))
    n=input("Enter the name:")
    c=input("Enter the course:")
    p=input("Enter the phone number:")
    e=input("Enter the email id:")
    f=input("Enter whether the fee is paid:")
    cur.execute("insert into student values(%s,'%s','%s','%s','%s','%s')"%(r,n,c,p,e,f,))
    ans=input("Do you want to continue:")
mycon.commit()
cur.execute("select * from student")
for i in cur:
    print(i)
