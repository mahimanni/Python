s1=input("Enter 1 word:")
s2=input("Enter 2 word:")
if(len(s1)==len(s2)):
    for i in range(len(s1)):
        flag=0
        for j in range(len(s2)):
            if(s1[i]==s2[j]):
               flag=1
        if(flag!=1):
            print("NO,The words are not anagrams")
            break
    else:#else clause
        print("YES,Words are anagrams")
else:
    print("NO,The words are not anagrams")     
