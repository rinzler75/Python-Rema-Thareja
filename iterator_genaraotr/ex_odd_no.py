class Odd:
    def __iter__(self):
        self.val=1
        return self
    def __next__(self):
        val=self.val
        self.val+=2
        return self.val
o=Odd()
count=0
#for i in o:
#    print(i,end=" ")
#    if count==10:
#        break
#    count+=1
for i in o:
    print(next(o),end=' ')
    if o.val==21:
        break

