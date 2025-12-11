import math

# Base class
class Shape:
    def __init__(self):
        pass

    def area(self):
        # Abstract method to be overridden
        raise NotImplementedError("Subclasses must implement the area() method")


# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


# Demonstration of polymorphism
if __name__ == "__main__":
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.area()}")
