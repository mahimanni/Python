l=[]
n=int(input("Enter no. of elements in the list:"))
for i in range(n):
    l.append(int(input(f"Enter {i+1} ele:")))

evenl=list(filter(lambda x:x%2==0,l))
oddl=list(filter(lambda x:x%2==1,l))

print("Even list of numbers=",evenl)
print("Odd list of numbers=",oddl)
