def rev(s):
    r=""
    for i in range(len(s)-1,-1,-1):
        r=r+s[i]
    return r

s=input("Enter string:")
l=[]
str=""
s=s+" "
ns=""

for i in range(len(s)):
    if(s[i]!=" "):
        str=str+s[i]
    else:
        l.append(rev(str))
        str=""

for i in range(len(l)):
    ns=ns+l[i]+" "

print("After reversing all the words in the string: ",ns)    
