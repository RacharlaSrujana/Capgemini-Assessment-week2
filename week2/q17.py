'''Implement an abstract class `ICalculator` with methods `add()`, `subtract()`, `multiply()`, and `divide()`. Create a `BasicCalculator` 
class that implements these methods.'''

from abc import ABC,abstractmethod
class ICalculator(ABC):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    @abstractmethod
    def add():
        pass
    @abstractmethod
    def subtract():
        pass
    @abstractmethod
    def multiply():
        pass
    @abstractmethod
    def divide():
        pass

class BasicCalculator(ICalculator):
    def __init__(self, a, b):
        super().__init__(a, b)
    def add(self):
        result=self.a+self.b
        print(f"Addition : {result}")
    def subtract(self):
        result=self.a-self.b
        print(f"Substraction : {result}")
    def multiply(self):
        result=self.a*self.b
        print(f"Multiplication : {result}")
    def divide(self):
        result=self.a/self.b
        print(f"Division : {result}")
basiccalculator=BasicCalculator(int(input("Enter a : ")),int(input("Enter b : ")))
basiccalculator.add()
basiccalculator.subtract()
basiccalculator.multiply()
basiccalculator.divide()