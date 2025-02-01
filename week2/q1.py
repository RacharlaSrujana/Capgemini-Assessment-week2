'''Create a class `Employee` with properties `name`, `id`, and `department`. Instantiate an object and assign values dynamically.'''

class Employee:
    def __init__(self,id,name,department):
        self.id=id
        self.name=name
        self.department=department
    def show_details(self):
        print(f"id : {self.id}, Name : {self.name}, Department : {self.department}")
e1=Employee(int(input()),input(),input())
e1.show_details()