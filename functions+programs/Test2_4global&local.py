'''
#This function uses global variable s
def func():
    print("Inside Function",s)

#Global Scope
s="Hello"
func()
print("Outside function",s)
'''

a=10
def fun1():
    #a=50#Inside: 50 Outside: 10
    print("Inside:",a)
    '''a=50
    UnboundLocalError: cannot access local variable 'a'
    where it is not associated with a value'''
fun1()
print("Outside:",a)
#Inside: 10
#Outside: 10
