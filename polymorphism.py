from abc import abstractmethod
import math
class Shapes:
    @abstractmethod
    def area(self):
        pass


class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Square(Shapes):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side **2

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2

class Pizza(Circle):
    def __init__(self, toppings,radius):
        super().__init__(radius)
        self.toppings= toppings


shapes=[Circle(4), Square(5), Triangle(6,7),Pizza("Pepperoni",15)]

for shape in shapes:
    print(f"{shape.area()}cm^2")