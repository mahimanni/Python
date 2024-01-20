s="HELLO"
a=5
for x in range(5):
    for i in range(a):
        print(s[i],end="")
    a=a-1    
    for j in range(0,x):
        print(s[j],end="")
    print()    

        
