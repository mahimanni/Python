s=input("Enter a string:")
freq={}
for i in s:#iterating over the string
    if i not in freq:#checking element in dictionary
        freq[i]=1
    else:
        freq[i]+=1

maxv=None
for k,v in freq.items():
    if(maxv==None):
        maxv=v
        maxvkey=k
    if(v>maxv):
        maxv=v
        maxvkey=k

print("Frequency of character ",maxvkey," that occured the most is ",maxv)        
