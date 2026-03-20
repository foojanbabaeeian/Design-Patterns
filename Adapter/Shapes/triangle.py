import right_triangle
import shape
class Triangle(shape.Shape):
    def __init__(self, base, height):
        self._triangle = right_triangle.RightTriangle(base, height)

    def area(self):
        return self._triangle.calc_area()

    def perimeter(self):
        return self._triangle.base + self._triangle.height + self._triangle.calc_hypotenuse()