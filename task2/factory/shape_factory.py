from shapes.init import Circle, Triangle

class ShapeFactory:
    @staticmethod
    def create_circle(radius: float) -> Circle:
        return Circle(radius)
    
    @staticmethod
    def create_triangle(a: float, b: float, c: float) -> Triangle:
        return Triangle(a, b, c)