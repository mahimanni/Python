l=[]
n=int(input("Enter the no of elements in list:"))
for i in range(n):
    l.append(input(f"Enter {i+1} string element of list:"))

nl=[]
for i in range(n):
    str=""
    a=l[i]
    for j in range(1,len(a)-1):#to remove first and last character of each string element
        str=str+a[j]
    nl.append(str)

print("New list consisting of strings with their first and last character removed:\n",nl)    
