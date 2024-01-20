#printing list of overlapping keys of two dictionaries
l=[]
d1=eval(input("Enter first dictionary: "))
d2=eval(input("Enter second dictionary: "))
for k1 in d1:
    for k2 in d2:
        if(k1==k2):
            l.append(k1)
print("List of Overlapping Keys are:",l)   
