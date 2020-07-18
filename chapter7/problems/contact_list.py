import os

with open("A:\\python\\chapter7\\problems\\contact_list.txt",'w') as file:
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
        with open("A:\\python\\chapter7\\problems\\contact_list.txt",'a') as file:
            c_no=input("Enter the contact number: ")
            c_name=input("Enter contact name: ")
            file.write("%-10s    %-20s\n"%(c_no,c_name))
   
   
    elif ch==2:
        with open("A:\\python\\chapter7\\problems\\contact_list.txt",'r') as file:
            with open("A:\\python\\chapter7\\problems\\temp.txt",'w') as file1:
                del_n=input("Enter the number of employee whose record has to be deleted: ")
                buf="afkjla"
                while len(buf)!=0:
                    buf=file.readline()
                    if del_n in buf:
                        continue
                    else:
                        file1.write(buf)
        os.remove("A:\\python\\chapter7\\problems\\contact_list.txt")
        os.rename("A:\\python\\chapter7\\problems\\temp.txt","A:\\python\\chapter7\\problems\\contact_list.txt")
      
  
    elif ch==3:
        print("   1.NUMBER")
        print("   2.NAME")
        print("   3.BOTH NAME AND NUMBER")
        i=int(input("   Enter Your Choice again: "))
        if i==1:
            with open("A:\\python\\chapter7\\problems\\contact_list.txt",'r') as file:
                with open("A:\\python\\chapter7\\problems\\temp.txt",'w') as file1:
                    u_emp=input("Enter the contact number whose record has to be updated: ")
                    n_no=input("Enter the new number:")
                    buf="asfdjsldjf"
                    while len(buf)!=0:
                        buf=file.readline()
                        a=buf.split("    ")
                        if u_emp in buf:
                            file1.write("%-10s    %-20s\n"%(n_no,a[1]))
                            continue
                        else:
                            file1.write(buf)
        elif i == 2:
            with open("A:\\python\\chapter7\\problems\\contact_list.txt",'r') as file:
                with open("A:\\python\\chapter7\\problems\\temp.txt",'w') as file1:
                    u_emp=input("Enter the contact number whose record has to be updated: ")
                    n_name=input("Enter the new name:")
                    buf="asfdjsldjf"
                    while len(buf)!=0:
                        buf=file.readline()
                        a=buf.split("    ")
                        if u_emp in buf:
                            file1.write("%-10s    %-20s\n"%(a[0],n_name))
                            continue
                        else:
                            file1.write(buf)
        elif i==3:
            with open("A:\\python\\chapter7\\problems\\contact_list.txt",'r') as file:
                with open("A:\\python\\chapter7\\problems\\temp.txt",'w') as file1:
                    update_emp=input("Enter the contact number whose record has to be updated: ")
                    new_name=input("Enter the new contact name: ")
                    new_no=input("Enter the new contact number: ")
                    buf="asfdjsldjf"
                    while len(buf)!=0:
                        buf=file.readline()
                        if update_emp in buf:
                            file1.write("%-10s    %-20s\n"%(new_no,new_name))
                            continue
                        else:
                            file1.write(buf)
        os.remove("A:\\python\\chapter7\\problems\\contact_list.txt")
        os.rename("A:\\python\\chapter7\\problems\\temp.txt","A:\\python\\chapter7\\problems\\contact_list.txt")
       

    elif ch==4:
        with open("A:\\python\\chapter7\\problems\\contact_list.txt",'r') as file:
            chk=file.readline()
            if chk=="":
                print("List empty Please enter some contacts..")
            buf="asfhkjshda"
            while len(buf)!=0:
                buf=file.readline()
                print(buf)

    
    
    elif ch==5:
        i=100                 