def GCD(x,y):
    if(x<y):#if x is not greater than y
        x=x+y
        y=x-y
        x=x-y
    if(x%y==0):
        return(y)
    else:
        return(GCD(y,x%y))

m=int(input("Enter 1 no:"))
n=int(input("Enter 2 no:"))
print("GCD of the two numbers is:",GCD(m,n))
    
    
