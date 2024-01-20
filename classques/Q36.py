l=[]
n=int(input("Enter the no of elements in list:"))
for i in range(n):
    l.append(int(input(f"Enter {i+1} list element:")))

value=int(input("Enter value whose indexes are to be searched:"))
print("Original list is:",l)

count=0
print("1-based Indexes of ",value," are:")
for i in range(0,n):
    if(l[i]==value):
        print(i+1)
        count+=1
if(count==0):
    print("Value not found.")

print("Value is repeated ",count," times in the list.")    
