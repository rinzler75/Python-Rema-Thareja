import math
class NegativeError(Exception):
    pass
num=int(input("Enter a num: "))
try:
    if num<0:
        raise NegativeError
    else: 
        print(" Square root of", num," is : ",math.sqrt(num))
except NegativeError as e:
    print("Square root of negative number cannot be found.....Program Terminating")