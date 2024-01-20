s=input("Enter string:")
news=""
for i in range(len(s)):
    #In 1-based indexing odd indexes are the even indexes in 0-based indexing
    if(i%2==0):
        pass
    else:
        news=news+s[i]
print("After removing the characters which have odd indexes:",news)        
