#calculating the size of the files in python37 folder do remember only files
import os
totalSize=0
for file in os.listdir("C:\\Python\\Python37"):
    totalSize+=os.path.getsize(os.path.join("C:\\Python\\Python37",file))
print("Total Size :",totalSize)

#check if the flash drive is connected
print(os.path.exists("G:\\"))
    