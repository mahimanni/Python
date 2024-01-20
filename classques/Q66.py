def less_than(list,k):
    nl=[x for x in list if x<k]
    return nl

n=int(input("Enter no of items in the list:"))
l=[]
for i in range(n):
    l.append(int(input(f"Enter {i+1} number of list:")))
k=int(input("Enter value of k:"))

nl=less_than(l,k)
print("List of numbers less than k from the original list:\n",nl)

    
