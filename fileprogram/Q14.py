#create dict with months as keys and no. of days in months as their values
d={'January':31,'February':28,'March':31,'April':30,'May':31,'June':30,
   'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
print("Created dictionary is:",d)

#enter month name and tell days of month
monthname=input("Enter the month name:")
for i in d:
    if(i==monthname):
        print(f"Days in {monthname} are ",d[i])
        break
else:
    print("No such month name found")
print()

#key in alphabetical order
l=[]
for i in d:
    l.append(i)
l.sort()
print("Keys in alphabetical order:",l)
print()
#or print("Keys in alphabetical order:",sorted(d))

#all month with 31 days
print("Months with 31 days are:",end=" ")
for i in d:
    if(d[i]==31):
        print(i,end=' ')
print()

#key value pair sorted by no of day in each month
daymonthlist=[]
print("\nKey value pairs sorted by no of days(values)")  
for i in d:
    daymonthlist.append([d[i],i])
daymonthlist.sort()

monthdaylist=[]
for i in daymonthlist:
    monthdaylist.append([i[1],i[0]])#square brackets imp

sorteddict=dict(monthdaylist)
print(sorteddict)        
