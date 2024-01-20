import math

class Shape:
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass

#class Circle created
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def calculate_area(self):
        return math.pi*(self.radius**2)

    def calculate_perimeter(self):
        return 2*math.pi*self.radius

#class Rectangle created
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def calculate_area(self):
        return self.length*self.width

    def calculate_perimeter(self):
        return 2*(self.length+self.width)

circleobj=Circle(5)
rectangleobj=Rectangle(4,6)

print("Area of Circle: ",circleobj.calculate_area(),"\nPerimeter of circle: ",circleobj.calculate_perimeter())
print("Area of Rectangle: ",rectangleobj.calculate_area(),"\nPerimeter of rectangle: ",rectangleobj.calculate_perimeter())


      
