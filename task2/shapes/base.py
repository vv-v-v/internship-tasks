from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass
    
    def is_right_angled(self) -> bool:
        return False