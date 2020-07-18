#example of formatting character
i=1
print("%-4s%-6s%-7s%-8s%-13s%-15s%-17s%-19s%-21s%-23s"%('i','i**2','i**3','i**4','i**5','i**6','i**7','i**8','i**9','i**10'))
while(i<=10):#for each i they are putting specified character 
    print("%-4d%-6d%-7d%-8d%-13d%-15d%-17d%-19d%-21d%-23d"%(i,i**2,i**3,i**4,i**5,i**6,i**7,i**8,i**9,i**10))
    i+=1
#for ex here for i they are putting 4 gaps
#again for i**2 they are putting 6 gaps in which whole exponent thing is coming