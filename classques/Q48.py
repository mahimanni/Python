s=input("Enter a word:")
rev=""
for i in range(len(s)-1,-1,-1):
    rev=rev+s[i]
print("Palindrome of the given word:",rev)    
