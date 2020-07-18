list=[1,2,3,4]
#here ur list is an iterable
it=iter(list) #here it is iterator
print(it.__next__())#prints next available element in the iterator
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__()) #u will see here StopIteration exception is generated
