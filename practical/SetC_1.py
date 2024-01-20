s=input("Enter string:")
str=""
l=[]
s=s+" "
for i in range(len(s)):
     if(s[i]!=" "):
         str=str+s[i]
     else:
         l.append(str)
         str=""

for i in range(len(l)-1,-1,-1):
    print(l[i],end=" ")
