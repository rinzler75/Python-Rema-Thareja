employee={'Ravi Kumawat':{'roll_no': '1ox17cs079','course':'cse'},'navnit kumar':{'roll_no': '1ox17cs063','course':'cse'}}
for key,value in employee.items():
    print("Name: ",key," Details: ",value)

## and prob 36
import random
a=set()
b=set()
for i in range(10):
    a.add(random.randint(1,100))
for i in range(6):
    b.add(random.randint(1,100))
print(a)
print(b)
print("a union b: ",a|b)
print("a intersection b: ",a&b)
print("a -b",a-b)
print("Symmetric difference: ",a^b)