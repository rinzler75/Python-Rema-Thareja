import os

with open("A:\\python\\chapter7\\problems\\record.txt",'w') as file:
    file.write("")

i=0
ch=0

while i!=100:
    print()
    print("*******MENU********")
    print()
    print("1.Add a new record")
    print("2.Delete a record")
    print("3.Update a record")
    print("4.Display all record")
    print("5.EXIT")
    ch=int(input("Enter your choice: "))


    if ch==1:
        with open("A:\\python\\chapter7\\problems\\record.txt",'a') as file:
            emp_no=input("Enter the employee number: ")
            emp_name=input("Enter employee name: ")
            file.write("%-10s    %-20s\n"%(emp_no,emp_name))
   
   
    elif ch==2:
        with open("A:\\python\\chapter7\\problems\\record.txt",'r') as file:
            with open("A:\\python\\chapter7\\problems\\temp.txt",'w') as file1:
                del_emp=input("Enter the name of employee whose record has to be deleted: ")
                buf="afkjla"
                while len(buf)!=0:
                    buf=file.readline()
                    if del_emp in buf:
                        continue
                    else:
                        file1.write(buf)
        os.remove("A:\\python\\chapter7\\problems\\record.txt")
        os.rename("A:\\python\\chapter7\\problems\\temp.txt","A:\\python\\chapter7\\problems\\record.txt")
      
  
    elif ch==3:
        with open("A:\\python\\chapter7\\problems\\record.txt",'r') as file:
            with open("A:\\python\\chapter7\\problems\\temp.txt",'w') as file1:
                update_emp=input("Enter the employee name whose record has to be updated: ")
                new_name=input("Enter the new employee name: ")
                new_no=input("Enter the new employee number: ")
                buf="asfdjsldjf"
                while len(buf)!=0:
                    buf=file.readline()
                    if update_emp in buf:
                        file1.write("%-10s    %-20s\n"%(new_no,new_name))
                        continue
                    else:
                        file1.write(buf)
        os.remove("A:\\python\\chapter7\\problems\\record.txt")
        os.rename("A:\\python\\chapter7\\problems\\temp.txt","A:\\python\\chapter7\\problems\\record.txt")
       

    elif ch==4:
        with open("A:\\python\\chapter7\\problems\\record.txt",'r') as file:
            buf="asfhkjshda"
            while len(buf)!=0:
                buf=file.readline()
                print(buf)
    
    
    elif ch==5:
        i=100                 