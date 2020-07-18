a=0
b=1
n=int(input("Enter the number of terms: "))
i=2
List=[a,b]
while i<n:
    s=a+b
    List.append(s)
    a=b
    b=s
    i+=1
print(List)
print("Sum: ",sum(List))

#-------------------------------------------------
#fibonnacci using dictionaries
Dict={0:0,1:1}
def fib(n):
    if n not in Dict:
        val=fib(n-1)+fib(n-2)
        Dict[n]=val
    return Dict[n]
n=int(input("Enter the value of n: "))
print("Fib(",n,")",fib(n))