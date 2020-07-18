#not executing have to search for the mistakes
def counter():
    val=0
    while True:
        yield val
        val+=1
        if val==10:
            raise StopIteration

c=counter()
for i in range(11):
    try:
       print(next(c),end=" ")
    except StopIteration:
        print("OVER")
        