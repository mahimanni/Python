s=input("Enter String:")
if(ord(s[0])>=97 and ord(s[0])<=122):
    str=chr(ord(s[0])-32)
else:
    str=s[0]

for i in range(1,len(s)):
    if(s[i-1]==' '):
        str=str+chr(ord(s[i])-32)
    else:
        str=str+s[i]
    
print("New String is after capitalizing first letter of each word of the string: ",str)    
    
