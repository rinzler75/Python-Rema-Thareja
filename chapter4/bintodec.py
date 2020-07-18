# binary to decimal number conversion
binary = int(input("Enter the binary number: "))
dec=0
i=0
while(binary!=0):
	remainder=binary%10
	dec=dec+(remainder*(2**i))
	binary=binary/10
	i=i+1
print("The decimal equivalent is : ",dec)
	
