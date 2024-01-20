eid=input("Enter email-id:")
c=0
domain=""
for i in range(len(eid)):
    if(eid[i]=='@'):
        c=1
    if(c==1):
        domain=domain+eid[i]
if(domain=="@gmail.com"):
    print("Valid e-mail")
else:
    print("Invalid e-mail")
        
        
