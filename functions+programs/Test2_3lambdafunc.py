#t=lambda x:x*2
#print("result:",t(9))

'''
#passing lambda func as an argument to a regular function
def func(f,n):
    print(f(n))

twice=lambda x:x*2
thrice=lambda x:x*3

func(twice,4)
func(thrice,3)
'''

#lambda func with argument is caluclated and returned
def increment(y):
    return((lambda x:x+1)(y))
a=100
print("a=",a)
print("a after incrementing=",increment(a))
