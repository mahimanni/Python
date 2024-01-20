l=[]
n=int(input("Enter the number of items of list:"))
for i in range(n):
    l.append(int(input(f"Enter {i+1} element:")))
x=int(input("Enter item to be removed:"))
nl=[]
for i in range(n):
    if(l[i]!=x):
        nl.append(l[i])
print("After removing all occurence of ",x,": ",nl)      

