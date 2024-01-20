'''
#** kwargs eg1
def printname(**name):
    print(type(name))
    print('Hello, ',name["fname"],name["mname"],name["lname"])

printname(mname="Kumar",lname="Sharma",fname="Rishu")    
'''

'''
#** kwargs eg2
def total_fruits(**fruit):
    print(fruit, type(fruit),sep='\n')

total_fruits(banana=5,mango=7,apple=8)    
'''

'''
#** kwargs eg3
def total_fruits(**fruit):
    total=0
    for amount in fruit.values():
        total+=amount
    return total

print("Total fruits=",total_fruits(banana=5,mango=7,apple=8))
'''
