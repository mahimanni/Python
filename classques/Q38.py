l=[]
n=int(input("Enter the no of elements in list:"))
for i in range(n):
    l.append(int(input(f"Enter {i+1} list element:")))

sum=0
for i in range(0,n):   
    sum+=l[i]
mean=sum/n

print("Mean of given list of numbers:",mean)
    
