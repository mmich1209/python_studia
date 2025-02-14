class Shape:
    pass

class Rectangle(Shape):
    pass

class Circle(Shape):
    pass

class Triangle(Shape):
    pass

figures = [Rectangle(), Circle(), Triangle()]

for figure in figures:
    print(type(figure))