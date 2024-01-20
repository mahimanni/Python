#remove duplicate values of a dict
d1=eval(input("Enter dictionary:")) 
print("Original dict:",d1)
l=[]
res={}
for k,v in d1.items():
     if v not in l:
          l.append(v)
          res[k]=v
print("Dictionary after removing duplicate values:",res)  
