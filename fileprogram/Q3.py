l=[]
n=int(input("Enter the number of elements of list:"))
for i in range(n):
    l.append(input(f"Enter {i+1} string element of list:"))
nl=[]    
for i in range(n):
    if(l[i]!="" and l[i]!=" "):
        nl.append(l[i])
print("After removing empty strings from the list strings: ",nl)       
    
