l=[]
n=int(input("Enter the no of elements in list:"))
for i in range(n):
    l.append(int(input(f"Enter {i+1} list element:")))

min=l[0]
max=l[0]
min_index=1
max_index=1
for i in range(1,n):
    if(l[i]<min):
        min=l[i]
        min_index=i+1
    if(l[i]>max):
        max=l[i]
        max_index=i+1

print("Max value is ",max," found at ",max_index," (1-based indexing)")        
print("Min value is ",min," found at ",min_index," (1-based indexing)")        
        
       
