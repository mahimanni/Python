#using super keyword
'''class Parent:
    def func1(self):
        print("This is function1")
        
class Child(Parent):
    def func2(self):
        super().func1()
        print("This is function2")
        
obj=Child()
obj.func2()'''

'''
class Person:
    def __init__(self,fname,lname):
        print("__init__ method of Person class")
        self.fname=fname
        self.lname=lname
    def printname(self):
        print("printname method of Person class")
        print(self.fname,self.lname)
        
class Student(Person):
    def __init__(self,fname,lname):
        print("__init__ method of Student class")
        super().__init__(fname,lname)
        super().printname()
        
x=Student("Mishi","Verma")
#x.printname()
'''

'''
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        Animal.sound(self)#calling base class overridden method using class name....classname.overriddenmethod()
        #super().sound()#calling base class overridden method using super()....super().overriddenmethod()
        print("Dog barks")

d=Dog()
d.sound()
#Animal makes sound
#Dog barks
'''
        



         
