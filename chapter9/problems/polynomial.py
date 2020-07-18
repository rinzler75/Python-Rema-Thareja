class polynomial:
    poly1=[]
    poly2=[]
    add=[]
    sub=[]
    large=0
    def display():
        ch=0
        while(ch!=5):
            print('''                     1. READ
                     2. ADD
                     3. SUBTRACT
                     4. DISPLAY RESULT
                     5. EXIT ''')
            ch=int(input("Enter ur choice: "))
            if ch==1:
                n=int(input("Enter the highest degree of first polynomial: "))
                for i in range(0,n+1):
                    polynomial.poly1.append(int(input("Enter the coefficient of x^ %d:"%i)))
                m=int(input("Enter the highest degree of second polynomial: "))
                for i in range(0,m+1):
                    polynomial.poly2.append(int(input("Enter the coefficient of x^ %d:"%i)))
            elif ch==2:
                if n>m:
                    polynomial.large=n
                    for i in range(0,m+1):
                        polynomial.add.append(polynomial.poly1[i]+polynomial.poly2[i])
                    for j in range(i+1,n+1):
                        polynomial.add.append(polynomial.poly1[j])
                        print(polynomial.add)
                else:
                    polynomial.large=m
                    for i in range(0,n+1):
                        polynomial.add.append(polynomial.poly1[i]+polynomial.poly2[i])
                    for j in range(i+1,m+1):
                        polynomial.add.append(polynomial.poly2[j])
                        print(polynomial.add)
            elif ch==3:
                if n>m:
                    polynomial.large=n
                    for i in range(0,m+1):
                        polynomial.sub.append(polynomial.poly1[i]-polynomial.poly2[i])
                    for j in range(i+1,n+1):
                        polynomial.sub.append(polynomial.poly1[j])
                    print(polynomial.sub)
                else:
                    polynomial.large=m
                    for i in range(0,n+1):
                        polynomial.sub.append(polynomial.poly1[i]-polynomial.poly2[i])
                    for j in range(i+1,m+1):
                        polynomial.sub.append(polynomial.poly2[j])
                    print(polynomial.sub)
            elif ch==4:
                print('''                     1. ADD RESULT
                         2. SUBTRACT RESULT''')
                k=int(input("Choice: "))
                if k==1:
                    h=polynomial.large
                    polynomial.add.reverse()
                    for i in polynomial.add:
                        print(i,"x^",h,"+",end=" ")
                        h-=1
                    print()

                elif k==2:
                    h=polynomial.large
                    polynomial.sub.reverse()
                    for i in polynomial.add:
                        print(i,"x^",h,"+",end=" ")
                        h-=1
                    print()
polynomial.display()
                
                              