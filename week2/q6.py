'''Implement a multi-level inheritance example where `Vehicle` is a base class, `Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` 
    inherits from `Car`.'''

class Vehicle:
    def __init__(self,wheels,speed):
        self.wheels=wheels
        self.speed=speed
class Car(Vehicle):
    def __init__(self, wheels, speed,seats):
        super().__init__(wheels, speed)
        self.wheels=wheels
        self.speed=speed
        self.seats=seats
    def show_car(self):
        print(f"Car details : \n Wheels : {self.wheels} \n Speed : {self.speed} \n Seats : {self.seats}")
class Bike(Vehicle):
    def __init__(self, wheels, speed,color):
        super().__init__(wheels, speed)
        self.wheels=wheels
        self.speed=speed
        self.color=color
    def show_bike(self):
        print(f"Bike details : \n Wheels : {self.wheels} \n Speed : {self.speed} \n Color : {self.color}")
class ElectricCar(Car):
    def __init__(self, wheels, speed, seats,version,charging):
        super().__init__(wheels, speed, seats)
        self.wheels=wheels
        self.speed=speed
        self.seats=seats
        self.version=version
        self.charging=charging
    def show_electric_car(self):
        print(f"Electric Car details : \n Wheels : {self.wheels} \n Speed : {self.speed} \n Seats : {self.seats} \
              \n version : {self.version} \n Charging : {self.charging}")

electriccar=ElectricCar(4,"1 Km/hr",7,"v9","3 hours")
electriccar.show_electric_car()
bike=Bike(2,"50 m/hr","red")
bike.show_bike()
car=Car(4,"12 km/hr",5)
car.show_car()