l=[]
n=int(input("Enter no. of elements in the list:"))
for i in range(n):
    l.append(int(input(f"Enter {i+1} ele:")))

squarel=list(map(lambda x:x**2,l))
cubel=list(map(lambda x:x**3,l))

print("Square element list:",squarel)
print("Cubed element list:",cubel)
