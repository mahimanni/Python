l=[['H',1,1,1],['Li',3,2,1],['Be',4,2,2,],['Na',11,3,1],['Mg',12,3,2],['K',19,4,1],['Ca',20,4,2],['Sc',21,4,3],['Ti',22,4,4],['V',23,4,5],['Cr',24,4,6],['Mn',25,4,7],['Fe',26,4,8],['Co',27,4,9]]

l[0].append("Non Metal")
l[1].append("Alkali Metal")
l[3].append("Alkali Metal")
l[5].append("Alkali Metal")

l[2].append("Alkaline earth Metal")
l[4].append("Alkaline earth Metal")
l[6].append("Alkaline earth Metal")

l[7].append("Transition Metal")
l[8].append("Transition Metal")
l[9].append("Transition Metal")
l[10].append("Transition Metal")
l[11].append("Transition Metal")
l[12].append("Transition Metal")
l[13].append("Transition Metal")

#Displaying all info stored about any element by entering it's symbol
symbol=input("Enter element symbol to see it's all info")
for i in l:
    if(i[0]==symbol):
        print("Symbol: ",i[0])
        print("Atomic Number: ",i[1])
        print("Row no: ",i[2])
        print("Column no: ",i[3])
        print("Property: ",i[4])
        break
else:
   print("No such symbol found.")

#Choose a property and list all elements in the table possessing that property
property=input("Enter property from the given options:\n1.Non Metal\n2.Alkali Metal\n3.Alkaline earth Metal\n4.Transition Metal\n")
print("All elements possessing the same property:")
for i in l:
    if(i[4]==property):
        print(i)


#Displaying all elements of particular row and column entered by user
row=int(input("Enter row:"))
print("All elements of row",row,"are:")
for i in l:
    if(i[2]==row):
        print(i)
        
column=int(input("Enter column:"))
print("All elements of column",column,"are:")
for i in l:
    if(i[3]==column):
        print(i)
