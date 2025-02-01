'''Create an interface `IShape` with an abstract method `calculate_area()`. Implement it in `Rectangle` and `Circle` classes.'''

from abc import ABC,abstractmethod
class IShape(ABC):
    @abstractmethod
    def calculate_area():
        pass
class Rectangle(IShape):
    def calculate_area(self):
        print(f"Area of rectangle : {5*4}")
class Circle(IShape):
    def calculate_area(self):
        print(f"Area of circle : {3.14 * 6 * 6:.2f}")
rectangle=Rectangle()
rectangle.calculate_area()
circle=Circle()
circle.calculate_area()