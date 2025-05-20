

class Shapes:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}")


class Circle(Shapes):

    def __init__(self, radius, color, is_filled):
        super().__init__(color, is_filled)
        self.radius = radius

    #Methond Overwriting
    def describe(self):
        print(f"It is a circle with area of {3.14*self.radius* self.radius}cm squared")
        super().describe()

class Square(Shapes):
    def __init__(self, width, color, is_filled):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with area of {self.width* self.width}cm squared")
        super().describe()

class Triangle(Shapes):
    def __init__(self, width,height,color,is_filled):
        (super().__init__(color, is_filled))
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with area of {self.width* self.height}cm squared")
        super().describe()

circle=Circle(0.3,'red',True)
square=Square(0.3,'blue',True)
triangle=Triangle(0.3,0.6,'yellow',True)


square.describe()