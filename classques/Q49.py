def prime(n):
    for i in range(2,(n//2)+1):
        if(n%i==0):
            return 0
    return 1

l=[]
n=int(input("Enter no of elements in list:"))
for i in range(n):
    l.append(int(input(f"Enter {i+1} element:")))
    
for i in range(n):
    if(prime(l[i])==0):
        print("False")
        break
else:
    print("True")
    
    
        
