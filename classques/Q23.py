s=input("Enter message:")
key=int(input("Enter key value:"))
es=""
ds=""

#Encryption
for i in range(len(s)):
    value=ord(s[i])+key#adding key to each character
    if(s[i]==" "):
        es=es+" "
    elif(((value<=90)&(value>=65))|((value<=122)&(value>=97))):
        es=es+chr(value)
    elif(value>90):
        a=64+(value-90)
        es=es+chr(a)
    elif(value>122):
        a=96+(value-122)
        es=es+chr(a)
print("Encrypted message is:\n",es)

#Decryption
for i in range(len(es)):
    value=ord(es[i])-key#subtracting key from each character
    if(es[i]==" "):
        ds=ds+" "
    elif(((value<=90)&(value>=65))|((value<=122)&(value>=97))):
        ds=ds+chr(value)
    elif(value<65):
        b=91-(65-value)
        ds=ds+chr(b)
    elif(value<97):
        b=123-(97-value)
        ds=ds+chr(b)
print("Decrypted message is:\n",ds)
        
