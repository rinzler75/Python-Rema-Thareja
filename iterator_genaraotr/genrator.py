def Square():
    number=2
    while True:
        yield number #this is different from return as the control doesnt come outside
        #an iterator is use to access this function 
        number*=number
Sq=Square()
print(next(Sq))
print(next(Sq))

#----------------------------------------ex.2
#hello world 
def print_Msg():
    yield("Hello")
    yield("World")
gen=print_Msg()
for i in gen:
    print(i,end=' ')
#---------------------------------------------reverse a string
def reverse(mes):
    length=len(mes)
    for i in range(length-1,-1,-1):
        yield mes[i]
mes='Hello'
print(" ")
for char in reverse(mes):
    print(char,end=' ')

