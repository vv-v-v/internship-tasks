import pytest
import math
from shapes.init import Circle

class TestCircle:
    def test_creation_valid(self):
        circle = Circle(5.0)
        assert circle.radius == 5.0

    def test_creation_invalid_radius(self):
        with pytest.raises(ValueError):
            Circle(-1)
        with pytest.raises(ValueError):
            Circle(0)

    def test_area_calculation(self):
        assert Circle(1.0).calculate_area() == math.pi
        assert Circle(2.0).calculate_area() == 4 * math.pi

    def test_not_right_angled(self):
        assert not Circle(5.0).is_right_angled()