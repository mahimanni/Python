s=input("Enter string:")
str=s[0]
x=s[0]
for i in range(1,len(s)):
    if((s[i] not in x)&(ord(s[i])-1!=ord(s[i]))):
       str=str+s[i]
       x=x+s[i]
print("Desired string:",str)       
