class Shape:
    color = ""
    area = 0

    def __init__(self):
        self.color = "red"
        self.area = 0
    
    def display_color(self):
        print("Colour is " + self.color)
    
    def area(self):
        print("Area is " + str(self.area))


class Circle(Shape):
    radius = 0

    def __init__(self,radius):
        super().__init__()
        self.radius = radius
    
    def calculateArea(self):
        ar = 3.14 * (self.radius ** 2)
        print("Area of Circle is " + str(ar) + " meter square. ")


def main():

    obj1 = Circle(7)

    obj1.display_color()
    obj1.calculateArea()

main()
    
    