List=[]
n=int(input("Enter the number of elements to be inserted in the list: "))
for i in range(n):
    print("Enter the number ",i+1)
    num=int(input())
    List.append(num)
print("Sorted list is: ","."*7)
List=sorted(List)
print(List)
i=len(List)-1
if n%2!=0:
    print("Median = ",List[i//2])
else:
    print("Median = ",(List[i//2]+List[i+1//2])/2)
