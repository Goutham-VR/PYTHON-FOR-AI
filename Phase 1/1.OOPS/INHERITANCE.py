# INHERITANCE

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Woof Woof")

D=Dog()
D.eat()
D.bark()

# Constructor Inheritance

class Animal:
    def __init__(self,name):
        self.name=name

class Dog(Animal):
    pass

d=Dog("Buddy")
print(d.name)

# Eg1
class Vehicle:
    def __init__(self,name):
        self.name=name

    def show_brand(self):
        print(f"Brand:{self.name}")

class Car(Vehicle):
    def start(self):
        print(f"Car is starting")

c=Car("Toyota")
c.show_brand()
c.start()

# Method Overriding
# Sometimes the parent class has a method, but the child wants a different version.
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

d=Dog()
d.sound()

# both has sound method, but the child class method will be called. This is called method overriding.

class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def work(self):
        print("Writing code")

dev=Developer()
dev.work()

# Eg1 
class Person:
    def introduce(self):
        print("I am a person")

class Student(Person):
    def introduce(self):
        print("I am a student")

s=Student()
s.introduce()

# How can the child call the parent's method?
# The answer is super().

class Person:
    def introduce(self):
        print("I am a person")

class Student(Person):
    def introduce(self):
        super().introduce() # calling the parent class method
        print("I am a student")

s=Student()
s.introduce()

# Parent Constructor
class Person:
    def __init__(self,name):
        self.__name=name # private attribute

    @property #getter method python way
    def name(self):
        return self.__name

class Student(Person):
    def __init__(self,name,course):
        super().__init__(name)# calling the parent constructor
        self.course=course

    def display(self):
        print(f" Name:{self.name}") # calling the parent getter method
        print(f" Course:{self.course}") # calling the child class attribute

s=Student("Alice","Math")
s.display()