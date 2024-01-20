def sum(l):
    s=0
    for i in l:
        s=s+i
    return(s)

ml=[]
m=int(input("Enter number of list elements in nested list"))
for i in range(m):
    l=[]
    n=int(input(f"Enter no of elements in {i+1} list:"))
    for j in range(n):
       l.append(int(input(f"Enter {j+1} element:")))
    ml.append(l)

print("Sample lists are :")
for i in range(m):
    print(ml[i],end=" ")

max=sum(ml[0])
maxpos=0
for i in range(1,m):
    if(sum(ml[i])>max):
        max=sum(ml[i])
        maxpos=i

print("\nList whose sum of elements is the highest:",ml[maxpos])        
    
 
