import pytest
from shapes.base import Shape
from calc.geometry_calculator import GeometryCalculator

def test_adding_new_shape():
    class Square(Shape):
        def __init__(self, side: float):
            if side <= 0:
                raise ValueError("Side must be positive")
            self.side = side
        
        def calculate_area(self) -> float:
            return self.side ** 2
        
        def is_right_angled(self) -> bool:
            return True
    
    square = Square(5)
    assert square.calculate_area() == 25
    assert square.is_right_angled()
    assert GeometryCalculator.calculate_area(square) == 25
    assert GeometryCalculator.is_right_angled(square)