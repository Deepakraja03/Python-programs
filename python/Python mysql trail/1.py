import mysql.connector as m
def ci():
    mycon=m.connect(host='localhost',user='root',passwd='2029',database='college')
    print(mycon.is_connected())
    cur=mycon.cursor()
    cur.execute('drop table student')
    cur.execute('''create table student(RollNo integer primary key,Name varchar(30) not null,Course varchar(30),Phone_Number char(10),EmailID varchar(35),Fee varchar(10))''')
    cur.execute('desc student')
    for i in cur:
        print(i)
    cur.execute('''insert into student(RollNo,Name,Course,Phone_Number,EmailID,Fee)
                   values(605001,'Adithya','B.E.Computer Science','9765434560','adithya254@gmail.com','Paid')''')
    cur.execute('''insert into student(RollNo,Name,Course,Phone_Number,EmailID,Fee)
                   values(605002,'Aniruth','B.E.Mechanical','8455702345','AniRuth@gmail.com','Not Yet')''')
    cur.execute('''insert into student(RollNo,Name,Course,Phone_Number,EmailID,Fee)
                   values(605003,'Caroline','Aeronautical Engineering','9853450864','Carolineforbes@gmail.com','Paid')''')
    cur.execute('''insert into student(RollNo,Name,Course,Phone_Number,EmailID,Fee)
                   values(605004,'Damon Salvatore','Civil Engineering','9758346578','damonsalvator1839@gmail.com','Paid')''')
    cur.execute('''insert into student(RollNo,Name,Course,Phone_Number,EmailID,Fee)
                   values(605005,'Niklaus','B.E.Computer Science','7299375700','Hopeklaushayley@gmail.com','Paid')''')
    mycon.commit()
    cur.execute('select * from student')
    for i in cur:
        print(i)
    mycon.close()
def upd():
    mycon=m.connect(host='localhost',user='root',passwd='2029',database='college')
    print(mycon.is_connected())
    cur=mycon.cursor()
    print("\n\n\t\tProgram to update student table")
    print("\n\t\tDisplaying the student table\n")
    cur.execute("select * from student")
    for i in cur:
        print(i)
    r=int(input("\nEnter the rollno for whom you want to change the phone number: "))
    p=input("\nEnter the new phone number: ")
    t=(p,r)
    cur.execute("update student set Phone_Number=%s where RollNo=%s",t)
    mycon.commit()
    cur.execute("select * from student")
    print("\n\n")
    for i in cur:
        print(i)
    mycon.close()
def ser():
    mycon=m.connect(host='localhost',user='root',passwd='2029',database='college')
    print(mycon.is_connected())
    cur=mycon.cursor()
    print("\n\n\t\tProgram to update student table")
    print("\n\t\tDisplaying the student table\n")
    cur.execute("select * from student")
    for i in cur:
        print(i)
    r=input("Enter the name of the student to be searched: ")
    t=(r,)
    cur.execute("select * from student where Name=%s",t)
    d=cur.fetchall()
    print("No of matching records:",len(d))
    if len(d)==0:
        print("Record Not Found.")
    else:
        for i in d:
            print(i)
    mycon.close()
def delt():
    mycon=m.connect(host='localhost',user='root',passwd='2029',database='college')
    print(mycon.is_connected())
    cur=mycon.cursor()
    print("\n\n\t\tProgram to delete student present in student table")
    print("\n\t\tDisplaying the student table\n")
    cur.execute("select * from student")
    for i in cur:
        print(i)
    r=input("Enter the name of the student to be deleted:")
    t=(r,)
    cur.execute("select * from student where Name=%s",t)
    d=cur.fetchall()
    print("No of matching records:",len(d))
    if len(d)==0:
        print("Record Not Found.")
    else:
        cur.execute("delete from student where Name=%s",t)
    print("Displaying student table after deleting the record")
    cur.execute("select * from student")
    for i in cur:
        print(i)
    mycon.close()
b=input("Enter Y/y to proceed with the program:")
while b=='y' or b=='Y':
    print("Enter 1 to create and insert")
    print("Enter 2 to update")
    print("Enter 3 to search")
    print("Enter 4 to delete a record")
    print("Enter 5 to exit")
    a=input("Enter your choice(1-5):")
    if a=='1':
        ci()
    elif a=='2':
        upd()
    elif a=='3':
        ser()
    elif a=='4':
        delt()
    elif a=='5':
        break
    else:
        print("The entered choice is invalid")
