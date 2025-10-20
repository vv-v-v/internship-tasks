import math
from shapes.init import Circle, Triangle
from calc.geometry_calculator import GeometryCalculator

class TestGeometryCalculator:
    def test_calculate_area_different_shapes(self):
        circle = Circle(2.0)
        triangle = Triangle(3, 4, 5)
        
        assert GeometryCalculator.calculate_area(circle) == 4 * math.pi
        assert GeometryCalculator.calculate_area(triangle) == 6.0

    def test_is_right_angled_different_shapes(self):
        circle = Circle(2.0)
        triangle = Triangle(3, 4, 5)
        non_right_triangle = Triangle(2, 3, 4)
        
        assert not GeometryCalculator.is_right_angled(circle)
        assert GeometryCalculator.is_right_angled(triangle)
        assert not GeometryCalculator.is_right_angled(non_right_triangle)

    def test_process_shapes(self):
        shapes = [Circle(1.0), Triangle(3, 4, 5), Circle(2.0)]
        areas = GeometryCalculator.process_shapes(shapes)
        expected = [math.pi, 6.0, 4 * math.pi]
        
        for actual, expected in zip(areas, expected):
            assert actual == expected