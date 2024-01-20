s=input("Enter string:")
l=[]
for i in range(len(s)):
    for j in range(len(s)):
        if((s[i]==s[j])&(i!=j)):
            break
    else:
            l.append(s[i])

print("Non-repeating characters in given string are:")
for i in range(len(l)):
    print(l[i],end=" ")
            
