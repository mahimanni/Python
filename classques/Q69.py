def unique(l):
    nl=[]
    for i in range(len(l)):
        for j in range(len(l)):
            if((l[i]==l[j])&(i!=j)):
                break
        else:
            nl.append(l[i])
    return(nl)

l=[]
n=int(input("Enter the no of items in the list:"))
for i in range(n):
    l.append(int(input(f"Enter {i+1} ele of list:")))

print("New list with unique ele of first list:\n",unique(l))

    
                       
