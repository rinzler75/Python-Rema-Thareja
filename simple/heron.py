a=float(input("Enter the first side of the triangle: "))
b=float(input("Enter the second side of the triangle: "))
c=float(input("Enter the third side of the triangle: "))
print(a,b,c) #alternate use of the print statement
S=(a+b+c)/2
area=(S*(S-a)*(S-b)*(S-c))**0.5 #to calculate square root
print("Area = " +str(area))

#adding: converting a floating point value into a int value
print("The integer variant of area is "+str(int(area)));

#finding ascii
c = input("Enter a character: ")
print("The ASCII value of '" + c + "' is",ord(c)) #ord is used to find the ASCII value of the character provided
