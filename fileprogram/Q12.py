def total(p,q,r):
    return(p+q+r)
def avg(p,q,r):
    return(((p+q+r)/3))

tl=[]
al=[]
l=[]
for i in range(5):#There are 5 students so 5 elements in nested tuple
    newl=[]
    for j in range(3):
        #each tuple element of nested tuple contains 3 elements(marks for 3 subject)
        newl.append(int(input(f"Enter {i+1} student {j+1} marks:")))
    newtup=tuple(newl)
    tl.append(total(newtup[0],newtup[1],newtup[2]))
    al.append(avg(newtup[0],newtup[1],newtup[2]))
    l.append(newtup)
tup=tuple(l)
print("Nested tuple : ",tup)

for i in range(5):
    print("Tuple element: ",tup[i]," Total marks: ",tl[i]," Average marks: ",al[i])
    
