import pprint
msg='I have merlin'
count={}
for i in msg:
    count.setdefault(i,0)
    count[i]+=1
pprint.pprint(count)