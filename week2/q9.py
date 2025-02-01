'''Simulate multiple inheritance where `FlyingCar` inherits from both `Car` and `defAirplane`. Handle potential conflicts in the `move()` 
   method.'''

class Car:
    def move1(self):
        print("Car moves on the road")
class DefAirplane:
    def move2(self):
        print("Airplane moves in the air")
class FlyingCar(Car,DefAirplane):
    def move(self):
        print("Flyingcar consists the features of both car and airplane")
flyingcar=FlyingCar()
flyingcar.move1()
flyingcar.move2()
flyingcar.move()