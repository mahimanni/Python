l=[]
n=int(input("Enter number of elements in list:"))
for i in range(n):
    l.append(int(input(f"Enter {i+1} element")))

max=l[0]
maxprev=max
for i in range(1,n):
    if(l[i]>max):
       maxprev=max
       max=l[i]

if(max==l[0]):#if 1st number(0th position number) is the maximum
    maxprev=l[1]
    for i in range(1,n):#not including 0th element as it is the maximum in this case
        if(l[i]>maxprev):
            maxprev=l[i]

print("Second largest number in the list:",maxprev)           
