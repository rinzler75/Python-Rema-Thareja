#working with the reduce function for three variables as the two variable is allready given in the book

import functools
num_list=[1,2,3,4,5]
print("Sum of the values in list: ")
print(functools.reduce(lambda x,y:x+y,num_list)) #or u can define one more function in the code


#map example
squares=[]
squares=list(map(lambda x:x**2,range(1,11)))
print("List of squares in the range 1-10",squares)
sum=0
for i in squares:
    sum+=i
print("Sum of squares in the range 1-10 = ",sum)

#append
num_list=[]
for i in range(1,11):
    num_list.append(i) #appends the values from back side
print("Original List: ",num_list)
for index,i in enumerate(num_list): #enumerate gives two values in index it provides the index while in the
    if i%2==0:                      #i it provides the values
        del num_list[index]
print("List after deleting even numbers: ",num_list)
 
 #enumerate oriented program
num_list=[1,2,3,4,5,6,5,4,3,2,1]
num=int(input("Enter the values to be searched: "))
count=0
for index,i in enumerate(num_list):
    if num==i:
        print(num,"found at location",index)
        count+=1
print(num,"appears",count,"times in list")

#combining the words
list_words=[]
for x in ["Hello","World"]:
        for y in ["Python","Programming"]:
                word=x+" "+y
                list_words.append(word)
print("List combining the words in two individual lists is: ",list_words)

#to remove all the duplicates from a list
num_list=[1,2,3,4,5,6,7,6,5,4]
print("Original list is: ",num_list) #or u can directly use set() function to get the distinct values
i=0
while i<len(num_list):
        num=num_list[i]
        for j in range(i+1,len(num_list)):
                val=num_list[j]
                if val==num:
                        num_list.pop(j)
        i+=1
print("List after removing the duplicates: ",num_list)
num_list.reverse() #can reverse the list by inbuilt function
print("Reversed list is : ",num_list)

#the shortcut method to make a list of odd number
l=[2*i+1 for i in range(20)]
print(l)

#filter example is over here
def is_positive(x):
        if x>=0: return 1
num_list=[10,-20,30,-40,50,-60,70,-80,90,-100]
List=[]
List=list(filter(is_positive,num_list)) #easily u can avoid using loops by using filter() and map()
print("Positive values list ",List)     #functions

#shortcut method for multiple values
n=[(x,y) for x in [10,20,30,50] for y in [35,40,55,60] if y%x==0]#here it can be taken as two for loops
#one inside the another
print(n)


#using reduce function to find the largest in the list
def large(x,y):
        if x>y:return x
        else: return y
num_list=[4,1,8,2,9,3,0]
print("The largest value is : ",functools.reduce(large,num_list)) #only provides with two values of the
#lists 

#putting lambda functions inside the list
L=[lambda x:x*2,lambda x: x*3,lambda x:x*4]
for i in L:
        print(i(5),end=" ") #5 is normally provided as the value is provided to lambda function
print("\nMultiplying the value of 100 by two: ",L[0](100))

