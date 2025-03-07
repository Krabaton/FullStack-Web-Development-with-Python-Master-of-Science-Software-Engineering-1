from abc import ABC, abstractmethod
from enum import Enum


class TypeShape(str, Enum):
    circle = "circle"
    square = "square"
    rect = "rect"


class Drawing(ABC):
    @abstractmethod
    def draw_shape(self, x, y, shape):
        pass


class DrawingRed(Drawing):
    def draw_shape(self, x, y, shape):
        print(f"Red drawing a {shape} at {x} and {y}")


class DrawingBlue(Drawing):
    def draw_shape(self, x, y, shape):
        print(f"Blue drawing a {shape} at {x} and {y}")


class DrawingGreen(Drawing):
    def draw_shape(self, x, y, shape):
        print(f"Green drawing a {shape} at {x} and {y}")


class Shape(ABC):
    def __init__(self, x, y, drawing: Drawing):
        self.x = x
        self.y = y
        self.drawing = drawing

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        self.drawing.draw_shape(self.x, self.y, TypeShape.circle)


class Square(Shape):
    def draw(self):
        self.drawing.draw_shape(self.x, self.y, TypeShape.square)


class Rect(Shape):
    def draw(self):
        self.drawing.draw_shape(self.x, self.y, TypeShape.rect)


if __name__ == "__main__":
    c = Circle(3, 3, DrawingRed())
    s = Square(10, 10, DrawingBlue())
    b = Square(5, 5, DrawingGreen())
    r = Rect(5, 5, DrawingGreen())

    c.draw()
    s.draw()
    b.draw()
    r.draw()
