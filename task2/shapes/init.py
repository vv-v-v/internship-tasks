from .base import Shape
from .validators import validate_positive

class Circle(Shape):
    def __init__(self, radius: float):
        validate_positive(radius, "Radius")
        self.radius = radius
    
    def calculate_area(self) -> float:
        import math
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, side_a: float, side_b: float, side_c: float):
        self._validate_sides(side_a, side_b, side_c)
        self.sides = (side_a, side_b, side_c)
    
    def _validate_sides(self, a: float, b: float, c: float):
        from .validators import validate_positive, validate_triangle
        validate_positive(a, "Side A")
        validate_positive(b, "Side B")
        validate_positive(c, "Side C")
        validate_triangle(a, b, c)
    
    def calculate_area(self) -> float:
        import math
        a, b, c = self.sides
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    def is_right_angled(self) -> bool:
        import math
        a, b, c = sorted(self.sides)
        tolerance = 1e-10
        return math.isclose(a**2 + b**2, c**2, rel_tol=tolerance)