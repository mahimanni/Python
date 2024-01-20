def mean(t,n):
    s=0
    for i in range(0,n):
       s=s+t[i]
    m=s/n
    return(m)  

t=((1,2),(3,4.15,5.18),(7,8,12,1,5))
m1=mean(t[0],2)
m2=mean(t[1],3)
m3=mean(t[2],5)
x=(m1,m2,m3)
totalmean=mean(x,3)

print("Tuple is:",t) 
print("Means of 1 element:",m1)
print("Means of 2 element:",m2)
print("Means of 3 element:",m3)
print("Total mean is:",totalmean)
