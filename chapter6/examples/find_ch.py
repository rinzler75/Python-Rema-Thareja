def f(s,c,pos=0):
    index=pos
    while(index<len(s)):
        if s[index]==c:
            print(c,"Found in string at index: ",index)
            return
        else:
            pass
        index+=1
    print(c," not found")
        
str=input("Enter the string: ")
ch=input("Input the char to be found: ")
i=int(input("Enter the position it program should start finding(string starts from 0): "))
f(str,ch,i)