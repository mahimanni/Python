import random
number=int(input("Enter a number:"))
n=len(str(number))
a=''
b=''
for i in range(n):
    b=b+"9"
    if(i==0):
        a=a+"1"
    else:
        a=a+"0"

ai=int(a)
bi=int(b)
randomno=random.randrange(ai,bi+1)
print("Random no generated having exactly n digits not starting with 0 is",randomno)
