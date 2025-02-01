'''Build a `SmartPhone` class inheriting from `MobileDevice`, which in turn inherits from `Electronics`. Demonstrate method overriding and 
    attribute reuse.'''

class Electronics:
    def __init__(self,cost):
        self.cost=cost
    def type(self):
        print("Types of electronic gadjets : Laptop,Computer,Printers")
        print(f"Type : Mobile phone, Cost : {self.cost}")
class MobileDevice(Electronics):
    def __init__(self, cost,type_of_device):
        super().__init__(cost)
        super().type()
        self.type_of_device=type_of_device
    def type(self):
        print("Types of mobile devices : Telephone,Nokia phone,Smart phone")
        print(f"Type : {self.type_of_device}, Cost : {self.cost}")
class SmartPhone(MobileDevice):
    def __init__(self, cost, type_of_device,brand):
        super().__init__(cost, type_of_device)
        super().type()
        self.brand=brand
    def type(self):
        print(f"Cost : {self.cost}, Type : {self.type_of_device}, Brand : {self.brand}")

smartphone=SmartPhone(90000,"Foldable phone","Oppo")
smartphone.type()