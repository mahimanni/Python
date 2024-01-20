l=[]
n=int(input("Enter the no of elements in list:"))
for i in range(n):
    l.append(int(input(f"Enter {i+1} list element:")))

nl=[]
nl.append(l[n-1])#last index moved to first
for i in range(n-1):
    nl.append(l[i])

print("After rotating the elements of list:",nl)    
               
