l=[]
def even(x,y):
    if(x%2==0 and y%2==0):
       return 1
    else:
       return 0
    
n=int(input("Enter no of tuple elements:"))
count=0
for i in range(n):
    newl=[]
    for j in range(2):#Every tuple element of nested tuple is in form(a,b) 
        newl.append(int(input(f"Enter {j+1} element of {i+1} position")))
    newtup=tuple(newl)
    check=even(newtup[0],newtup[1])#checking both a,b are even
    if(check==1):
        count+=1
    l.append(newtup)
tup=tuple(l)
print("Nested tuple:",tup)
print("Number of pairs(a,b) of nested tuple such that a,b are even :",count)
