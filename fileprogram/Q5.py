l=[]
n=int(input("Enter the number of items of list:"))
for i in range(n):
    l.append(int(input(f"Enter {i+1} element:")))
sum=0
product=1
for i in range(n):
    sum+=l[i]
    product*=l[i]
print("Sum of all elements in list:",sum)
print("Product of all elements in list:",product)
