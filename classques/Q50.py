l=[]
n=int(input("Enter no of elements in list:"))
for i in range(n):
    l.append(int(input(f"Enter {i+1} element:")))

s=""
for i in range(n):
    s=s+str(l[i])

m=int(s)
print("After coverting a list of multiple integers into a single integer is:",m)

