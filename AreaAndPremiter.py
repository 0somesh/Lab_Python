import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def cal_circle_area(self):
        return math.pi * self.radius**2 # formula: π * r^2
    
    def cal_circle_perimeter(self):
        return 2 * math.pi * self.radius    # formula: 2π * r

radius = float(input("Input the radius of the circle: "))

circle = Circle(radius)

area = circle.cal_circle_area() 

perimeter = circle.cal_circle_perimeter() 

print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter) 
