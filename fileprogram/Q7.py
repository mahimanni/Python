s=input("Enter String:")
max=""
str=""
for i in range(len(s)):
    ch=s[i]
    if(((ord(ch)>=65 and ord(ch)<=90) or (ord(ch)>=97 and ord(ch)<=122))and(ch not in "aeiou") and (ch not in "AEIOU")):
          str=str+ch
    else:
          str=""
    if(len(str)>len(max)):
        max=str           
     
print("Longest substring of the given string having just the consonants:",max)         
