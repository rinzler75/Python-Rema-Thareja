stack=[]
ch=0
while(ch!=4):
    print("-------MENU-------------")
    print("1.PUSH")
    print("2.POP")
    print("3.DISPLAY")
    print("4.EXIT")
    ch=int(input("Enter your choice: "))

    if ch==1:
        ele=input("Enter the element to be inserted: ")
        stack.insert(0,ele) #u can also append which will insert the element at the last of the list
    elif ch==2:
        if len(stack)==0:
            print("STACK EMPTY")
        else:
            print("POPPED ELEMENT IS : ",stack.pop(0))#if pop is defined without index it will take last value
    elif ch==3:
        if len(stack)==0:
            print("STACK EMPTY")
        else:
            a=len(stack)
            for i in stack:
                print(i)
                
    
