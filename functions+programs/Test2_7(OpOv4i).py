class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def __gt__(self,other):
        return self.area()>other.area()

#create two rectangle objects
rect1=Rectangle(4,5)
rect2=Rectangle(3,6)

#check if the area of the first rectangle is greater than the second rectangle
result=rect1>rect2

print(f"Is the area of rectangle1 greater than rectangle2? {result}")
