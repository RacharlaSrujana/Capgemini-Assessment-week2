'''Develop a `Shape` class with a method `area()`. Implement `Square` and `Triangle` classes that provide specific implementations for `area()`.'''

class Shape:
    def area(self):
        print("The area method is present in parent class Shape")
class Square(Shape):
    def area(self,side):
        super().area()
        print(f"Area of square : {side * side}")
class Triangle(Shape):
    def area(self,base,height):
        print(f"Area of triangle : {0.5 * base * height}")
square=Square()
square.area(4)
triangle=Triangle()
triangle.area(10,5)