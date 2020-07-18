#basic functions using set
Coders=set(["Arnav","Goransh","Mani","Parul"])
Analysts=set(["Krish","Mehak","Shiv","Goransh","Mani"])
print("Coders: ",Coders)
print("Analysts: ",Analysts)
#Coders(intersection)analysts can be written as coders & analysts
print("People working as Coders as well as Analysts: ",Coders.intersection(Analysts)) 
#Coders U analysts coders | analysts
print("People working as Coders or analysts: ",Coders.union(Analysts)) 
#Coders - Analysts or if u want the other way u can write it as
#Analysts-Coders
print("People working as Coders but not Analysts:",Coders.difference(Analysts))
#Symmetric difference(A-B)+(B-A) not in mathematical terms but in set terms
#using operator u can use it as a^b
print("People working in only one of the groups: ",Coders.symmetric_difference(Analysts))


#----------------------------------------------------------------------------------------------------


#example no 1 that generates a set of prime numbers  and another set of odd numbers
odds=set([x*2+1 for x in range(1,10)])
print(odds)
primes=set()
#here this functions creates the primes number u need to remember it
for i in range(2,20):
    j=2
    flag=0
    while j<i/2:
        if i%j==0:
            flag=1
        j+=1
    if flag==0:
        primes.add(i)
        #this element gets added in only one condition if it is unique in the set 
        #u can use update() also if it is sequence 
print(primes)
print("UNION: ",odds|primes)
print("INTERSECTION: ",odds&primes)
print("SYMMETRIC DIFFERENCE:",odds^primes)
print("DIFFERENCE:",odds-primes)

#----------------------------------------------------------------------------------------------------
evens=set([2*x for x in range(1,10)])
print("EVENS: ",evens)
composites=set()
for i in range(2,22):
    j=2
    flag=0
    while j<=i/2:
        if i%j==0:
            composites.add(i)
        j+=1
print("COMPOSITES: ",composites)
#is superset means evens>=composites if composites belong to evens
#is subset means evens<=composites if evens belongs to composites
print("SUPERSET: ",evens.issuperset(composites))
print("ALL:",all(evens))
print("Length of the composite set: ",len(composites))
print("SUM OF ALL NUMBERS IN EVENS SET:",sum(evens))
#-------------------------------------------------------------------------------------------------------

#demonstrating the other functions such as pop(),update(),remove(),add(),clear()
squares=set([x**2 for x in range(1,10)])
cubes=set([x**3 for x in range(1,10)])
print("SQUARES: ",squares)
print("CUBES: ",cubes)
#for the sequence we use add or else update
squares.update(cubes)
#adding a single element
squares.add(11*11)
squares.add(11*11*11)
print("ADD: ",squares)
print("POP: ",squares.pop())
squares.remove(1331)
print("REMOVE: ",squares)
squares.clear()
print("CLEAR: ",squares)
#--------------------------------------------------------------------------------------------------------
#sorting the set
countries=['India','Russia','China','Brazil','England']
c_set=set(sorted(countries))
print(c_set)