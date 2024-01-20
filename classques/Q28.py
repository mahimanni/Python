s=input("Enter string:")
substr=input("Enter substring to be removed:")
news=""
j=0
if((substr!=" ") & (substr!="")):
    for i in range(len(s)):
        if(s[i]==substr[j]):
            a=i
            while((s[i]==substr[j])&(j<len(substr))):
                i+=1
                j+=1
                if(j==len(substr)-1):
                    break
            if(j!=len(substr)-1):
                i=a
                j=0
        news=news+s[i]
    print("After removing substring: ",news)
else:
    print("Entered string is empty.")
