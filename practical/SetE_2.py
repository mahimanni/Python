l=[]
print('Enter three digits:')
for i in range(3):
  l.append(int(input(f"{i+1} digit:")))

for i in range(0,3):
     for j in range(0,3):
           if(i!=j):
               for k in range(0,3):
                  if(j!=k & k!=i):
                      print(l[i],l[j],l[k],sep=" ")
           
      
