def rev(s):
    str=""
    for i in range(len(s)-1,-1,-1):
        str=str+s[i]
    return(str)    
  
s=input("Enter string:")
str=""
l=[]
s=s+" "
for i in range(len(s)):
     if(s[i]!=" "):
         str=str+s[i]
     else:
         l.append(rev(str))
         str=""
         
print("Reverse string:")
for i in range(len(l)):
    print(l[i],end=" ")
