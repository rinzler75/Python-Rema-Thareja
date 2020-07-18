List=[1,2,3,4]
print([x**2 for x in List])
nList=(x**2 for x in List) #generator expression
try:
    for i in range(10):
        print(next(nList),end=" ")
except StopIteration:
    print("over")