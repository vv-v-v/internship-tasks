from shapes.base import Shape

class GeometryCalculator:
    @staticmethod
    def calculate_area(shape: Shape) -> float:
        return shape.calculate_area()
    
    @staticmethod
    def is_right_angled(shape: Shape) -> bool:
        return shape.is_right_angled()
    
    @staticmethod
    def process_shapes(shapes: list[Shape]) -> list[float]:
        return [shape.calculate_area() for shape in shapes]