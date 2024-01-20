#Program to display the min and max value in dictionary
d=eval(input("Enter dictionary:")) 
print("Original dict:",d)
maxvalue=None
minvalue=None

#Iterating through the dictionary's values to find the max and min value
for i in d.values():
    #for the first value encountered set it to max and min
    if (maxvalue is None and minvalue is None):
        maxvalue=i
        minvalue=i
    else:
        if(i>maxvalue):
            maxvalue=i
        if(i<minvalue):
            minvalue=i

print("Maximum value of dictionary:",maxvalue)
print("Minimum value of dictionary:",minvalue)
