product={'medicine':240,'vegetables':360,'motivation':1000}
total_bill=0
while True:
    item=input("Item taken: ")
    if item=='-1':
        break
    for i in product.keys():
        if i==item:
            total_bill+=product[i]
print("The total bill is :",total_bill)    

#-----------------prob11
string=input("Enter the string: ")
string=string.lower()
string=sorted(list(string))
A={}
for i in string:
    if i not in A:
        A[i]=1
    else:
        A[i]+=1

print(A)
