import pytest
from shapes.init import Triangle

class TestTriangle:
    def test_creation_valid(self):
        triangle = Triangle(3, 4, 5)
        assert triangle.sides == (3, 4, 5)

    def test_creation_invalid_sides(self):
        with pytest.raises(ValueError):
            Triangle(0, 4, 5)
        with pytest.raises(ValueError):
            Triangle(1, 2, 10)

    def test_area_calculation(self):
        assert Triangle(3, 4, 5).calculate_area() == 6.0
        
    def test_right_angled(self):
        assert Triangle(3, 4, 5).is_right_angled()
        assert Triangle(5, 12, 13).is_right_angled()
        assert not Triangle(2, 3, 4).is_right_angled()