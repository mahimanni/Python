l=[]
n=int(input("Enter the no of elements in list:"))
for i in range(n):
    l.append(int(input(f"Enter {i+1} list element:")))

nl=[]
start=l[0]
i=0
while(i<n):
    a=[]
    while(start==l[i]):
        a.append(l[i])
        i+=1
        if(i==n):
          nl.append(a)#for appending the last consecutive duplicate list into nested list nl
          break

    if(i==n):
          break        
    nl.append(a)    
    start=l[i]

 
print("After packing consecutive duplicates of the list into subsets:\n",nl)    
