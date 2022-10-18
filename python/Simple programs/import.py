import pickle
def emp_function():
    empno=int(input("Enter the Employee number:"))
    name=input("Enter the Employee name:")
    salary=int(input("Enter the Employee's salary:"))
    insentive=int(input("Enter the Employee's insentive:"))
    total_sal=int(input("Enter the Employee total salary:"))

    emp_list=[]
    emp_list.append(empno)
    emp_list.append(name)
    emp_list.append(salary)
    emp_list.append(insentive)
    emp_list.append(total_sal)
def display(emp_function):
    print(display)
    file=open('emp.dat',"wb")
    pickle.dump(emp_list, file)
    pickle.flush()
    file.close()
def d():
    f=open('emp.dat','rb')
    a=f.read()
    print(a)
    f.close()
for i in range(100):
    a=input("Do you want to run this program(y/n):")
    if a=='y' or a=='Y':
        emp_function()
    elif a=='n' or a=='N':
        print("Thank You")
        break
    else:
        print("The entered value is not valid")
d()
