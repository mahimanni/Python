s=input("Enter string:")
ch=input("Enter character whose no of occurrences you want:")
#using inbuilt count function
#c=s.count(ch)

#without using inbuilt count function
c=0
for i in range(len(s)):
    if(s[i]==ch):
        c+=1
print("No of occurrences of given character:",c)       
