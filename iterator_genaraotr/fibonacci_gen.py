def fib():
    a,b=0,1
    while a<10:
        yield b
        a,b=b,a+b

iter = fib()
for i in iter:
    print(i,end=" ")

