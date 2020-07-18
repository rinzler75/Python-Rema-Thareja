import random
num_list=[]
for i in range(10):
    val=random.randint(1,100)
    num_list.append(val)
print("Original List: ",num_list)
even_list=[]
odd_list=[]
for i in num_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("Even number list is: ",even_list)
print("Odd number list is : ",odd_list)