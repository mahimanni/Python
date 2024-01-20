s=input("Enter String:")
str=""
i=0
a=0
while(i<len(s)):
     if(s[i]==' '):
          str=str+' '
          a=a+1
     if((ord(s[i])>=97 and ord(s[i])<=122) and a%2==0):
          str=str+chr(ord(s[i])-32)
     else:
          str=str+s[i]
     a=a+1     
     i=i+1     
print("New String after capitalizing every other letter in the string: ",str)          
          
