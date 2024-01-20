l=[]
n=int(input("Enter number of elements in list:"))
for i in range(n):
    l.append(int(input(f"Enter the {i+1} element:")))
for i in range(len(l)):
    if(l[i]%2==0):
        l[i]=l[i]**3
    else:
        l[i]=l[i]**2
print("List after converting odd no of the list into square and even to it's cube:",l)        
    
