def pangram(s):
    for i in range(65,91):
        flag=0
        for j in s:
            if((ord(j)==i)|(ord(j)==i+32)):
                flag=1
        if(flag==0):
            print("String ",s," is not a pangram string.")
            break
    else:
        print("String",s," is a pangram string.")
         
s=input("Enter string:")
pangram(s)
