from factory.shape_factory import ShapeFactory

class TestShapeFactory:
    def test_create_circle(self):
        circle = ShapeFactory.create_circle(5.0)
        assert circle.radius == 5.0

    def test_create_triangle(self):
        triangle = ShapeFactory.create_triangle(3, 4, 5)
        assert triangle.sides == (3, 4, 5)