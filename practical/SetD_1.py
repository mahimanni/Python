n=int(input("Enter a number:"))
s=str(n)
s1=""
for i in range(len(s)):
    if(s[i]!="0"):
        s1=s1+s[i]
n1=int(s1)
print(n1)
r=0
while(n1>0):
    a=n1%10
    r=a+(r*10)
    n1=n1//10
print("New number after removing zeroes then reversing:",r)    
