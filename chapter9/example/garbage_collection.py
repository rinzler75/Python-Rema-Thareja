var1=10 #creates object var1
var2=var1 #Increase ref count of var1- object assignment
var3=[var1] #Increase ref count of var 1 - reassignment
var2=50 #decrease ref count of var1 - assignment
var3[0]=1 #decrease ref count of var1-removal from list
del var1 #decrease ref count of var1-object deleted

#if the object loses its reference count to 0 then the object or a variable is automatically added to
#garbage collection and would not be allocated memory during allocation