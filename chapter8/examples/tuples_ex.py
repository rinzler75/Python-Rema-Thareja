toppers=("Janvi",[94,95,96,97])
print("Class topper: ",toppers[0])
print("Highest marks in 4 subjects: ",toppers[1:]) #this thing prints the whole list inside the tuple

#list comprehension inside the tuple
def double(T):
    return tuple([i*2 for i in T])
tup=(1,2,3,4,5)
print("Original Tuple: ",tup)
print("Double tuple",double(tup))

#swapping the values using tuple multiple assignment
val1=10
val2=20
print("val1=",val1,"val2=",val2)
(val1,val2)=(val2,val1) #swapped in one line
print("val1=",val1,"val2=",val2)
#for using without third variablel is
# x = x + y; // x now becomes 15 
#  y = x - y; // y becomes 10 
#   x = x - y;

#returning multiple values using tuple
PI=3.14
def cal_a_r(r):
    return (PI*(r**2),2*PI*r)
radius=float(input("Enter the radius: "))
(area,circumference)=cal_a_r(radius)
print("Area of the circle with radius",radius,"= ",area)
print("Circumference of the circle with radius",radius,"= ",circumference)

#gather and scatter
def display(*args): #gather
    print(args)
tup=(1,2,3,4,5)
display(tup) 

#scatter
tup=(56,3)
#values are now scattered and passed
quo,rem=divmod(*tup) #divmod(tup) will show error
print(quo,rem)

#email address
addr=input("Enter any email address: ")
user_name,domain_name=addr.split('@')
print("User Name :",user_name)
print("Domain Name :",domain_name)

#adding things to tuple
tup=(-10,12,-9,3,4,-8,5,6)
newTup=()
for i in tup:
    if i>0:
        newTup+=(i,)#addition between two tuples are possible
print(newTup)

#zip example
tup=(1,2,3,4,5)
List1=['a','b','c','d','e']
print(list((zip(tup,List1))))

ques=["Roll No","Name","Course"]#keys
ans=[7,"Saesha","BSc"]
for q,a in zip(ques,ans):
    print("What is ur ",q,"?")
    print("My",q,"is:",a)
