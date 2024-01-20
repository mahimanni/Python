s=input("Enter string:")
ns=""

for i in range(len(s)):
    a=ord(s[i])
    if((a>=65)&(a<=90)):
        ns=ns+chr(a+32)
    if((a>=97)&(a<=122)):
        ns=ns+chr(a-32)

print("String after converting all the characters of the word in Togglecase:",ns)        
