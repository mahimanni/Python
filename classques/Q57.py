A=set()
for i in range(1,11):
    A.add(i**2)#add() adds an single element to the set

B=set()
for i in range(1,11):
    B.add(i**3)

print("Set A after adding values:",A)
print("Set B after adding values:",B)

#sets are mutable, update() is used to add multiple elements to the set
#A.update(121,144)TypeError: 'int' object is not iterable
A.update((121,144))#you can update set with **list,**set,**keyvalues of dictionary
B.update((1331,1728))
print("\nSet A after updating it's values and adding squares of 11 and 12:",A)
print("Set B after updating it's values and adding cubes of 11 and 12:",B)

#remove() removes a particular item and raises an error if the item does not exist in the set
A.remove(144)
print("\nSet A after removing element 144:",A)
#A.remove(145)KeyError: 145
B.remove(1728)
print("Set B after removing element 1728:",B)
#B.remove(1729)KeyError: 1729

#discard() removes a particular item and does not raise an error if the item does not exist in the set
A.discard(121)
print("\nSet A after discarding element 121:",A)
A.discard(145)#gives no error
print("Set A after discarding element 145:",A)
B.discard(1331)
print("Set B after discarding element 1331:",B)
B.discard(1729)#gives no error
print("Set B after discarding element 1729:",B)

#pop() removes and returns an arbitrary set element and raises KeyError if the set is empty
print("\nA.pop()=",A.pop())
print("B.pop()=",B.pop())
