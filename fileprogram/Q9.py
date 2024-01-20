l=[]
n=int(input("Enter number of elements in list:"))
for i in range(n):
    l.append(int(input(f"Enter {i+1} element")))

freq={}
for i in l: #iterating over the list
    if i in freq: #checking the element in dictionary
        freq[i]+=1 #incrementing count
    else:
        freq[i]=1 #initializing the count
print("Frequencies of all elements of the list:")        
print(freq)#printing the frequency 

ul=[]
dl=[]
for i in range(n):
    p=0
    for j in range(n):
        if(l[i]==l[j] and i!=j):
            p=1
            break
    if(p==0):
        ul.append(l[i])  

for i in range(n):
    q=0
    for j in range(len(ul)):
      if(l[i]==ul[j]): 
        q=1
    if(q==0  and l[i] not in dl):    
       dl.append(l[i])          

print("List of Unique elements:",ul)
print("List of duplicate elements:",dl)


