import mysql.connector as m
mycon=m.connect(host='localhost',user='root',passwd='2029',database='college')
print(mycon.is_connected())
cur=mycon.cursor()
print("\n\n\t\tProgram to update student table")
print("\n\t\tDisplaying the student table\n")
cur.execute("select * from student")
for i in cur:
    print(i)

ans='Y'
while ans.upper()=='Y':
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
    ans=input("Do you want to continue the search:")
mycon.close()
