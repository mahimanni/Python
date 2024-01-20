n=int(input("Enter no upto which you eant to generate the series:"))
x=0
y=1
l=[]
l.append(x)
l.append(y)
for i in range(3,(n-2)+1):
    c=lambda a,b:a+b
    l.append(c)
    x=y
    y=c

print("Generated fibonacci series is:")
for i in range(n):
    print(l[i],end=",")
