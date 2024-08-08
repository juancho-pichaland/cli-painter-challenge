# TODO: Add code here
import pickle
import matplotlib.pyplot as plt
from math import pi

class Point:
    def _init_(self, x: float, y: float):
        self.x = x
        self.y = y

class Circle:
    def _init_(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def area(self) -> float:
        return pi * (self.radius ** 2)

    def draw(self) -> None:
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def _str_(self) -> str:
        return f"Circle with center at ({self.center.x}, {self.center.y}) and radius {self.radius}"

class Triangle:
    def _init_(self, point_1: Point, point_2: Point, point_3: Point):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    def area(self) -> float:
        return abs((self.point_1.x*(self.point_2.y - self.point_3.y) +
                    self.point_2.x*(self.point_3.y - self.point_1.y) +
                    self.point_3.x*(self.point_1.y - self.point_2.y)) / 2.0)

    def draw(self) -> None:
        x = [self.point_1.x, self.point_2.x, self.point_3.x, self.point_1.x]
        y = [self.point_1.y, self.point_2.y, self.point_3.y, self.point_1.y]
        plt.fill(x, y, color='b')
        plt.axis("scaled")
        plt.show()

    def _str_(self) -> str:
        return (f"Triangle with vertices at ({self.point_1.x}, {self.point_1.y}), "
                f"({self.point_2.x}, {self.point_2.y}), "
                f"and ({self.point_3.x}, {self.point_3.y})")

class Rectangle:
    def _init_(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2

    def area(self) -> float:
        width = abs(self.point_2.x - self.point_1.x)
        height = abs(self.point_2.y - self.point_1.y)
        return width * height

    def draw(self) -> None:
        x = [self.point_1.x, self.point_2.x, self.point_2.x, self.point_1.x, self.point_1.x]
        y = [self.point_1.y, self.point_1.y, self.point_2.y, self.point_2.y, self.point_1.y]
        plt.fill(x, y, color='g')
        plt.axis("scaled")
        plt.show()

    def _str_(self) -> str:
        return f"Rectangle with vertices at ({self.point_1.x}, {self.point_1.y}) and ({self.point_2.x}, {self.point_2.y})"

class Painter:
    FILE = ".painter"

    def _init_(self) -> None:
        self.shapes: list = []
        self._load()

    def _load(self) -> None:
        try:
            with open(Painter.FILE, "rb") as f:
                self.shapes = pickle.load(f)
        except (EOFError, FileNotFoundError):
            self.shapes = []

    def _save(self) -> None:
        with open(Painter.FILE, "wb") as f:
            pickle.dump(self.shapes, f)

    def add_shape(self, shape) -> None:
        self.shapes.append(shape)
        self._save()

    def total_area(self) -> float:
        return sum(shape.area() for shape in self.shapes)

    def clear(self) -> None:
        self.shapes = []
        self._save()
