#By using map function
l=[]
for i in range(1,31):
    l.append(i)
cubemf=list(map(lambda x:x**3,l))
print("By using map function:",cubemf)
