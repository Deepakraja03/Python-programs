import csv
f=open('e.csv','r')
a=csv.reader(f)
for i in a:
    print(i)
f.close()
