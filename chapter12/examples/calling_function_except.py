def Divide(num,deno):
    return num/deno
try:
    Divide(10,0)
#try block for the calling function
except ZeroDivisionError:
    print("You cannot divide a number by zero....Program Terminating......")