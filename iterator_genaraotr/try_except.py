#this block shows the use of try and except
import sys
list=[1,2,3,4]
it=iter(list)
while True:
    try: #this is try block looks for any exception like java
        print(next(it),end=' ')
    except StopIteration: #while this code is like catch block which will catch the the regarding exception
        print("\n All the elements have allready been accessed. No more elements ")
        sys.exit()
