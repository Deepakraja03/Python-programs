import mysql.connecter as myc
a = myc.connect(host = 'local host',user = 'Deepak',password = '2029',db = 'students')
mycur = a.cursur()
mycur.execute("show tables")
mycur.execute("select * from students")
b = mycur.fetchall()
for i in b:
    print(i)
a.close()



