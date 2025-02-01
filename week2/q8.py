'''Design a system where a base class `Animal` has a method `speak()`, and subclasses `Dog` and `Cat` override it.'''

class Animal:
    def speak(self):
        print("I am speak method from 'Animal' class")
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog says 'bow bow' as it is hungry")
class Cat(Animal):
    def speak(self):
        print("Cat says 'meow' as it feels hungry")

dog=Dog()
dog.speak()
cat=Cat()
cat.speak()