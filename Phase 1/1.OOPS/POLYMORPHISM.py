# One interface (same method name), many behaviors.
# Eg 1:
class Dog: #class 1
    def sound(self): # method sound
        print("Bark")

class Cat: #class 2
    def sound(self): # method sound, same as class 1
        print("Meow")

c=Cat()
d=Dog()
c.sound()
d.sound()

# This is called polymorphism. The same method name (sound) behaves differently based on the object (Dog or Cat).

# The Real Power
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")
 
animals = [Dog(), Cat()] # list of objects of different classes

for a in animals:
    a.sound()

# Real-World Example
class UPI:
    def pay(self):
        print("UPI Payment")

class CreditCard:
    def pay(self):
        print("Card Payment")

class Wallet:
    def pay(self):
        print("Wallet Payment")

payments = [UPI(), CreditCard(), Wallet()]

for p in payments:
    p.pay()