'''Create a multi-level class structure with `Person` → `Employee` → `Manager`, where `Manager` has an additional method `approve_leave()`.'''

class Person:
    def __init__(self,id,name):
        self.id=id
        self.name=name
class Employee(Person):
    def __init__(self, id, name,role,salary):
        super().__init__(id, name)
        self.role=role
        self.salary=salary
    def employee_details(self):
        print(f"id : {self.id} \n Name : {self.name} \n Role : {self.role} \n Salary : {self.salary}")
class Manager(Employee):
    def __init__(self, id, name, role, salary):
        super().__init__(id, name, role, salary)
    def approve_leave(self,reason):
        print("Manager is also an employee")
        print("Manage has the right to approve leave to the employees")
        if reason==" ":
            print("Manager doesnot approve leave")
        else:
            print("Manager approves leave")
manager=Manager(101,"Alice","Manager",90000)
manager.employee_details()
manager.approve_leave(" ")
