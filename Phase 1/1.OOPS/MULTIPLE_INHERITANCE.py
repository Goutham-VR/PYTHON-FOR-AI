# Animal <- Dog = One parent → One child - This is called Single Inheritance.
# A class can inherit from more than one parent. - This is called Multiple Inheritance.

class Father:
    pass

class Mother:
    pass

class Child(Father, Mother):
    pass

# Father ──┐
#           ├── Child
# Mother ──┘
# The child gets features from both parents.

# Eg 1
class Father: # Parent class 1
    def skill1(self):
        print("Driving")

class Mother: # Parent class 2
    def skill2(self):
        print("Cooking")

class Child(Father, Mother): # Child inherits from both Father and Mother
    pass

c = Child()

c.skill1()
c.skill2()

#Suppose both parents have the same method.
class Father:
    def show(self):
        print("Father")

class Mother:
    def show(self):
        print("Mother")

class Child(Father, Mother):
    pass

c = Child()
c.show()

# why?

# Python searches from left to right.

# Child
#  ↓
# Father
#  ↓
# Mother
#  ↓
# object

# It finds show() in Father first and stops.

#Example with Constructors

class Father:
    def __init__(self):
        print("Father Constructor")

class Mother:
    def __init__(self):
        print("Mother Constructor")

class Child(Father, Mother):
    pass

c = Child() # Father Constructor


class A:
    def show(self):
        print("A")

class B(A): # B inherits from A
    def show(self):
        print("B")

class C(A): # C inherits from A
    def show(self):
        print("C")

class D(B, C): # D inherits from B and C
    pass