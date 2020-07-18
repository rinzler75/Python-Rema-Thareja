import time
start= time.time()
def largest(n1,n2,n3):
    if(n1>n2 and n1>n3):
        print(n1,"LARGEST")
    elif(n2>n1 and n2>n3):
        print(n2,"LARGEST")
    else:
        print(n3,"LARGEST")
print("Enter the numbers to be checked: ")
num1=int(input())
num2=int(input())
num3=int(input())
largest(num1,num2,num3)
end=time.time()
print("--- %s seconds ---" % (end - start))