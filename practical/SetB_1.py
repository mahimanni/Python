n=int(input("Enter the number:"))
s=""


for i in range(0,10):
    m=n
    while(m>0):
        a=m%10
        if(a==i):
            s=s+str(a)
        m=m//10
        
    
b=int(s)
print("Number in ascending order is: ",b)
