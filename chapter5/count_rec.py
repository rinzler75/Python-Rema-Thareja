def func(n,count=0):#default parameterized fuction
    if n==0:
        return count
    else:
        return func(n-1,count+1)
print("No of times the recursive function is envoking: ",func(100))