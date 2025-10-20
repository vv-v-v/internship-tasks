def validate_positive(value: float, name: str):
    if value <= 0:
        raise ValueError(f"{name} must be positive")

def validate_triangle(a: float, b: float, c: float):
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("Triangle with these sides cannot exist")