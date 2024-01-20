s=input("Enter string:")
freq={}
for i in s:
    if(i not in freq):
        freq[i]=1
    else:
        freq[i]+=1
print("Count of frequencies of all the characters in the given string :\n",freq)        
