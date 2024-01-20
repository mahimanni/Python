'''
#indirect func call
def hello():
    print("Hello World")
x=hello
x()'''

'''#*args Non keyword arbitrary arguments eg1
def printname(*name):
     print("Hello, ",name[0],name[1],name[2])
printname("Rishu","Kumar","Sharma")'''   

'''
#0-based index tuple list check
t=(1,2,3,4,5)
print(t[4])
l=[7,8,9,10,11]
print(l[3])
'''

'''
#*args eg2
def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum+=i
    print("Average is:",sum/len(numbers))

average(5,6)    
average(5,6,7)
average(2,3,4,1)
'''
'''<class 'tuple'>
Average is: 5.5
<class 'tuple'>
Average is: 6.0
<class 'tuple'>
Average is: 2.5'''


'''
#*args eg3
def multiply(n):
  m=1
  for i in n:
      m=m*i
  return m

def call(multiply,*numbers):
    result=multiply(numbers)
    return result

print("Result=",call(multiply,3,4,5))#Result= 60
print("Result=",call(multiply,6,4,5))#Result= 120
'''

'''a=int(input("Enter no of ele in list whose multiplication of ele you want:"))
l=[]
for i in range(a):
    l.append(int(input(f"Enter {i+1} ele:")))

tup=tuple(l)    
print("Multiplication of all ele of list:",call(multiply,tup))'''    

