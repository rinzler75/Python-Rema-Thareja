class A:
    def __init__(self):
        self.a={}
    def count(self,sentence):
        for i in sentence:
            if i in self.a:
                self.a[i]+=1
            else:
                self.a[i]=1
        for i,j in self.a.items():
            print("%-2s :%s"%(i,"*"*j))
class B(A):
    def count(self,word):
        super().count(word)
        
a=A()
a.count(input("Enter the statement: "))
b=B()
b.count(input("Enter a word: "))

##output
#while writting ignore the hashes "#"
#Enter the statement: how are you
# h  :*
# o  :**
# w  :*
#    :**
# a  :*
# r  :*
# e  :*
# y  :*
# u  :*
# Enter a word: merlin
# m  :*
# e  :*
# r  :*
# l  :*
# i  :*
# n  :*
            