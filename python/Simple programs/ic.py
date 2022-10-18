import mysql.connector
mycon = mysql.connector.connect(host = "localhost" ,
                                user = "root" ,
                                passwd = "2029" ,
                                database = "school")
c = mycon.cursor()
c.execute("create table van (Roll_no integer , Name varchar(30))")
c.execute("insert into van(Roll_no,Name) values(12301,'Adi')")
data = c.fetchall()
count = c.rowcount
print("Total number of rows retrieved in result set:" , count)
for row in data:
    print(row)
