def swap(s):
    t=s[1]+s[0]
    for i in range(2,len(s)):
        t=t+s[i]
    return t

s1=input("Enter 1 string:")
s2=input("Enter 2 string:")

x=swap(s1)
#strings are immutable if s1 used instead of x then s1 will not change instead will now point to other string
y=swap(s2)
news=""
for i in range(len(x)):
    news=news+x[i]
news=news+" "
for j in range(len(y)):
    news=news+y[j]

print("Single string obtained is:",news)
