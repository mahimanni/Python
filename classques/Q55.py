def prime(n):
    X=set()
    count=0
    i=2
    while(count<n):
        for j in range(2,(i//2)+1):
            if(i%j==0):
                break
        else:
            X.add(i)
            count+=1
        i=i+1
    return(X)

def odd(m):
    Y=set()
    count=0
    i=1
    while(count<m):
        Y.add(i)
        count+=1
        i=i+2
    return(Y)    

def union_ud(X,Y):
    U=set()
    for i in X:
        U.add(i)
    for j in Y:
        for i in X:
            if(j!=i):
                U.add(j)
    return(U)

def intersection_ud(X,Y):
    I=set()
    for i in X:
        for j in Y:
            if((i==j)&(i not in I)):
                I.add(i)
    return(I)

def difference_ud(X,Y):
    D=set()
    for i in X:
        for j in Y:
            if(i==j):
                break
        else:
            D.add(i)
    return(D)            

A=set()
n=int(input("Enter number of elements in set A of prime numbers:"))
A=prime(n)
print("Set A is: ",A)

B=set()
m=int(input("Enter number of elements in set B of odd numbers:"))
B=odd(m)
print("Set B is: ",B)

#By user-defined functions
U=union_ud(A,B)
I=intersection_ud(A,B)
D=difference_ud(A,B)
SD=difference_ud(U,I)

print("\nResults by user-defined functions are:")
print("Union of sets are:",U)
print("Intersection of sets are:",I)
print("Difference of sets are:",D)
print("Symmetric Difference of sets are:",SD)

#By string inbuilt functions
U=A.union(B)
I=A.intersection(B)
D=A.difference(B)
SD=A.symmetric_difference(B)

print("\nResults by built-in functions are:")
print("Union of sets are:",U)
print("Intersection of sets are:",I)
print("Difference of sets are:",D)
print("Symmetric Difference of sets are:",SD)

print("\nResults by user-defined functions are:")
print("Union of sets are:",A|B)
print("Intersection of sets are:",A&B)
print("Difference of sets are:",A-B)
print("Symmetric Difference of sets are:",A^B)


