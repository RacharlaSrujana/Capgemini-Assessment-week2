'''Develop an interface `IVehicle` with abstract methods `start_engine()` and `stop_engine()`. Implement it in `Car`, `Bike`, and `Truck` classes.
'''

from abc import ABC,abstractmethod
class IVehicle(ABC):
    @abstractmethod
    def start_engine():
        pass
    @abstractmethod
    def stop_engine():
        pass
class Car(IVehicle):
    def start_engine(self):
        print("The car engine has started")
    def stop_engine(self):
        print("The car engine has stopped")
class Bike(IVehicle):
    def start_engine(self):
        print("The bike engine has started")
    def stop_engine(self):
        print("The bike engine has stopped")
class Truck(IVehicle):
    def start_engine(self):
        print("The truck engine has started")
    def stop_engine(self):
        print("The truck engine has stopped")
car=Car()
car.start_engine()
car.stop_engine()
bike=Bike()
bike.start_engine()
bike.stop_engine()
truck=Truck()
truck.start_engine()
truck.stop_engine()