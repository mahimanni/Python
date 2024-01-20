def search_many(s,x,k):
    if(k>0):
        count=0
        for i in s:
            if(i==x):
                count+=1
        if((count<=k)&(count!=0)):
            return True
        return False#if count is 0 or not atmost k
    else:
        return False#if k is not greater than 0

#for checking the function
l=[]
n=int(input("Enter no of elements in sequence:"))
for i in range(n):
    l.append(int(input(f"Enter {i+1} element:")))
x=int(input("Enter item to be searched:"))
k=int(input("Enter no of occurrences k:"))
print('Result:',search_many(l,x,k))
