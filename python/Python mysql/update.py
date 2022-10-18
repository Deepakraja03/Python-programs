import mysql.connector as m
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
