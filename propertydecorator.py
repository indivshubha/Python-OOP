
class Rectangle:
    def __init__(self,width,height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("width must be positive")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height must be positive")

rectangle = Rectangle(10,20)

rectangle.width=0


print(rectangle.width)
print(rectangle.height)

