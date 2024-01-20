def rev(n):
    r=0
    while(n>0):
      a=n%10
      r=a+(r*10)
      n=n//10
    return r
print("Palindrome numbers between 10 to 1000 are:")
for i in range(10,1001):
    if(rev(i)==i):
        print(i,end=", ")
