s=input("Enter string:")
x=""
for i in range(len(s)):
    if(s[i] in x):
        print("Not a unique string")
        break
    x=x+s[i]
else:
    print("Unique string")

