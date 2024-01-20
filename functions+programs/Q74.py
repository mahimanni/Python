l=[]
n=int(input("Enter no of ele in list:"))
for i in range(n):
    nl=[]
    nl.append(input(f"Enter {i+1} subject name:"))#to store name
    nl.append(int(input(f"Enter {i+1} subject marks:")))#converted to int as to store the marks
    tup=tuple(nl)
    l.append(tup)

print("Original list of tuples is:\n",l)

#sorting according to the marks
for i in range(0,n):
    for j in range(0,(n-1-i)):
        a=l[j]
        b=l[j+1]
        if(a[1]>b[1]):
            t=a
            a=b
            b=t
print("Resultant list is:",l)
