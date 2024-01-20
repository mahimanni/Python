l=[]
n=int(input("Enter number of elements in list:"))
for i in range(n):
    l.append(int(input(f"Enter {i+1} element")))

nl=[]
countzero=0
for i in range(n):
    if(l[i]!=0):
        nl.append(l[i])
    else:
        countzero+=1
        
while(countzero>0):
    nl.append(0)
    countzero-=1

print("After shifting all the zero to the right & non zero elements to the left:",nl)   

