ml=[]
m=int(input("Enter number of list elements in nested list"))
for i in range(m):
    l=[]
    n=int(input(f"Enter no of elements in {i+1} list:"))
    for j in range(n):
       l.append(int(input(f"Enter {j+1} element:")))
    ml.append(l)

print("Sample lists are :")
for i in range(m):
    print(ml[i])
