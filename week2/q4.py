'''Implement a `Student` class with a constructor that initializes `name` and `roll_number`. Write a method to return student details.'''

class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
    def student_details(self):
        print(f"Name : {self.name}, Roll Number : {self.roll_number}")
student1=Student("Alisa",1201)
student1.student_details()
student2=Student("Surya",1202)
student2.student_details()
student3=Student("Catharene",1203)
student3.student_details()