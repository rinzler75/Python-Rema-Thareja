#--------------------------------------------------------------------------------------------
#all the basic functions in one
Dict={'Roll_No':'1ox17cs092','Name':'Shivangi','Course':'BE-CSE'}
#ACCESSING VALUES are accessed using key value unlike other ds
print("Dict[Roll_No]=",Dict['Roll_No'])
#ADDING VALUES
Dict['Marks']=97.35
print("Modified Dict: ",Dict)   
#MODIFYING A VALUE
Dict['Roll_No']='1OX17CS063'
print("Modified Dict: ",Dict)
#DELETING A KEY-VALUE PAIR
del Dict['Course']
#or u can
print("Name is :",Dict.pop('Name'))
#now two values are deleted
print("Name is : ",Dict.pop('Name',"Unavailable"))#here -1 is default value if the key is not there in the dict 
#"unavailable" default value would be given
#randomly popping any element
print("Randomly popping any elements: ",Dict.popitem())
print("After deletion: ",Dict)
#clearing the whole dictionary but the variable will remain
Dict.clear()
print("After clear(),Dictionary has no items: ",Dict)
#clearing the variable itself
del Dict
#print(Dict) #error would be obtained

#-----------------------------------------------------------------------------------------
#looping over dictonary items
states={'Delhi':'DL','Haryana':'HR','Maharastra':'MH','Rajasthan':'RJ'}
states.setdefault('Karnataka','Sorry unavailable')
print("Code for rajasthan: ",states['Rajasthan'])
for i in states.items():
    print(i)
#if the key is not present in the dict get function prints the default values
print("Code for karnataka: ",states.get('Karnataka'))
print(states['Karnataka'])

#-------------------------------------------------------------
#creating a dicionary using comprehension
print("Enter -1 to exit............. ")
Circumference={}
while True:
    r=float(input("Enter radius: "))
    if r==-1:
        break
    else:
        Dict={r:2*3.14*r} #only way to update a dictionary
        Circumference.update(Dict)
print(Circumference)

#----------------------------------------------------------------------------------------
#dict comprehension
m_cm={x:x*100 for x in range(1,11)}
temp=m_cm.values()
cm_m={x:x/100 for x in temp}
print("Meters: Centimeters",m_cm)
print("Centimeters:Meters",cm_m)
Dict={x:x**3 for x in range(10) if x%2==1}
print(Dict)

#---------------------------------------------------------------------------------------------
#another way of accessing the elements
E_H={'Friends':'Mitr','Teacher':'Shikshak','Book':'Pustak'}
H_U={'Mitr':'Dost','Shikshak':'Adhyapak','Pustak':'Kitab'}
for i in E_H:
    print(i,"in Hindi Means ",E_H[i],"in urdu means ",H_U[E_H[i]])

#---------------------------------------------
#count the number of letter in statement
def count(message):
    letters_count={}
    for letter in message:
        letters_count[letter]=letters_count.get(letter,0)+1
    print(letters_count)
msg=input("Enter a message: ")
count(msg)

#----------------------------------------------------------------------------
#KEEP SPARSE MATRIX AS A DICTIONARY
matrix=[[0,0,0,1,0],
        [2,0,0,0,3],
        [0,0,0,4,0]]
Dict={}
print("Sparse Matrix")
for i in range(len(matrix)):
    print("\n")
    for j in range(len(matrix[i])):
        print(matrix[i][j],end=' ')
        if matrix[i][j]!=0:
            Dict[(i,j)]=matrix[i][j]
print("\n\n Sparse Matrix can be efficiently representes as Dictionary: ")
print(Dict)
#--------------------------------------
#inverting the values of the dictionary
Dict={'Roll_No':'1ox17cs092','Name':'Shivangi','Course':'BE-CSE'}
inverted={}
for key,val in Dict.items():
    inverted[val]=key
print("Dict: ",Dict)
print("Inverted Dict: ",inverted)
#____________________________________________________
Marks={'Neha':[97,89,94,90],'Mitul':[92,91,94,87],'Shefali':[67,99,88,90]}
tot=0
Tot_marks=Marks.copy()
for key,val in Marks.items():
    tot=sum(val)
    Tot_marks[key]=tot
print(Tot_marks)
max=0
Topper=' '
for key,val in Tot_marks.items():
    if val>max:
        max=val
        Topper=key
print("Topper is : ",Topper,"with Marks =",max)

#-----------------------------------------------------------------------------------------------------------
#frequency of histogram
#same program can be used with the file where u can take text from file to count number of character occurences 
#In the file
msg="Hello All,Good Morning......Welcome to the world of Python"
msg=msg.lower()
Dict=dict()
for word in msg:
    if word not in Dict:
        Dict[word]=1
    else:
        Dict[word]+=1
print(Dict)
for key,val in Dict.items():
    print(key,'\t','*'*val)

#-------------------------------------------------------------------------------------------------------------
#combining two lists to make a dictionary
keys=['Name','Age','Martial Status']
values=['Om',28,'Married']
details=zip(keys,values)
Dict=dict(details)
print(Dict)