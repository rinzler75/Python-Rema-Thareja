def add(*args): #variable length arguments and as you can see here
    '''Fuction returns the sum of values passed to it'''
    sum=0
    for i in args:
        sum+=i
    return sum
print(add.__doc__) # its double '_'
print("SUM= ",add(25,30,45,50))