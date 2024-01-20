l=[]
n=int(input("Enter no of items in original list"))
for i in range(n):
    l.append(input(f"Enter {i+1} element"))

cl=[]
m=int(input("Enter no of items in character list"))
for i in range(m):
    cl.append(input(f"Enter {i+1} element"))

nl=[]
for i in range(n):
    a=l[i]
    for j in range(len(l[i])):
        x=0
        for k in range(m):
            if(a[j]==cl[k]):
                x=1  
                break
        if(x==1):
            break
    if(x==0):  
        nl.append(a)    
                  
print('New list formed:',nl)
