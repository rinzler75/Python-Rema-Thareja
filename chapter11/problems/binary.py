class Binary:
    def convert_to_dec(self):
        binary = self.bin
        dec=0
        i=0
        while(binary!=0):
	        remainder=binary%10
	        dec=dec+(remainder*(2**i))
	        binary=int(binary/10)
	        i=i+1
        self.dec=dec
    
    def convert_to_bin(dec):
        q=dec
        b=[]
        while q!=(1 or 0):
            r=int(q%2)
            q=int(q/2)
            b.insert(0,r)
        b.insert(0,q)
        str1=""
        for i in b:
            str1+=str(i)
        b1=int(str1)
        return b1
            
    
    def __init__(self,bin):
        self.bin=bin
    
    def __iadd__(self,D):
        self.convert_to_dec()
        D.convert_to_dec()
        res=self.dec+D.dec
        self.bin=Binary.convert_to_bin(res)
        self.dec=res
        return self

a=Binary(11001)
b=Binary(1100100)
a+=b
print(a.bin)
print("decimal equivalent: ",a.dec)
    
	