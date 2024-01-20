A=set()
for i in range(1,11):
    if(i%2==0):
        A.add(i)#set A consists of even no in range 1-10

B=set()
B.add(1)
for i in range(2,21):
    flag=0
    for j in range(2,(i//2)+1):
        if(i%j==0):
            flag=1
            break
    if(flag==1):        
        B.add(i)

print("Set A of even numbers is:",A)
print("Set B of composite numbers is:",B)

#all() returns true if all the elements of iterable are true otherwise false
print("\nUse of all function:")
print("all(A):",all(A))
print("all(B):",all(B))

#A>=B returns true if B is a subset of A or A is a superset of B
print("\nUse of issuperset function:")
print("A>=B:",A.issuperset(B))
print("B>=A:",B.issuperset(A))

#returns sum of all elements in the iterable
print("\nSum of all elements in the set A:",sum(A))
print("Sum of all elements in the set B:",sum(B))
