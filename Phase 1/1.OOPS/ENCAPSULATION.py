# ============================================================
#                    ENCAPSULATION IN PYTHON
# ============================================================

# Encapsulation:
#
# It is the idea of controlling access to an object's data.
#
# Instead of letting any code freely modify important values,
# we decide what should be accessible and how it should be
# accessed or modified.
#
# Main concepts:
#
# 1. Public attributes     -> name
# 2. Protected attributes  -> _name
# 3. Private-ish attributes -> __name
# 4. Name mangling
# 5. Getter
# 6. Setter
# 7. Property
# 8. Inside class vs Outside class
# 9. pass


# ============================================================
# 1. PUBLIC ATTRIBUTES
# ============================================================

# Public attributes can normally be accessed and modified
# from anywhere.

class Student:

    def __init__(self):
        self.name = "Alice"       # Public


s = Student()

print(s.name)                    # OK
s.name = "Bob"                   # OK
print(s.name)


# ============================================================
# 2. PROTECTED ATTRIBUTES
# ============================================================

# A single underscore (_) is a convention.
#
# It means:
#
# "This attribute is intended for internal use.
#  Please don't access it directly."
#
# IMPORTANT:
# Python does NOT actually prevent access to protected attributes.


class Student:

    def __init__(self):
        self.name = "Alice"       # Public
        self._age = 20            # Protected


s = Student()

print(s.name)                    # OK
print(s._age)                    # Works
s._age = 25                      # Also works


# _age is protected only by CONVENTION.
#
# Python does not generate an AttributeError just because
# we access _age from outside.


# ============================================================
# 3. PRIVATE-ISH ATTRIBUTES
# ============================================================

# Double underscore (__) triggers NAME MANGLING.
#
# Example:
#
# self.__grade
#
# becomes approximately:
#
# self._Student__grade
#
# Python changes the name by adding:
#
# _ClassName
#
# This makes accidental access harder.
#
# IMPORTANT:
# __variable is NOT truly private in Python.


class Student:

    def __init__(self):
        self.name = "Alice"       # Public
        self._age = 20            # Protected
        self.__grade = "A"        # Private-ish


s = Student()

print(s.name)                    # OK
print(s._age)                    # Works
print(s.__grade)                 # ❌ AttributeError
#
# Why?
#
# Inside the class:
#
# self.__grade
#
# becomes:
#
# self._Student__grade
#
# There is no attribute literally called:
#
# __grade
#
# Therefore:
#
# print(s.__grade)
#
# gives AttributeError.


# ============================================================
# 4. PRIVATE VARIABLE WORKS INSIDE THE CLASS
# ============================================================

class Student:

    def __init__(self):
        self.name = "Alice"
        self._age = 20
        self.__grade = "A"

    def show(self):

        print(self.name)          # Public - works
        print(self._age)          # Protected - works
        print(self.__grade)       # Private-ish - works


s = Student()

s.show()


# Why does self.__grade work here?
#
# Because we are INSIDE the Student class.
#
# Python understands that:
#
# self.__grade
#
# means:
#
# self._Student__grade


# ============================================================
# 5. NAME MANGLING
# ============================================================

class Student:

    def __init__(self):
        self.__grade = "A"


s = Student()

# Internally, Python stores it approximately as:
#
# _Student__grade
#
# Therefore this technically works:

print(s._Student__grade)


# But this is NOT recommended.
#
# It breaks the intended encapsulation.
#
# Python is basically saying:
#
# "I made this name harder to access accidentally,
#  but I am not creating a security lock."


# ============================================================
# 6. IMPORTANT: __variable OUTSIDE THE CLASS
# ============================================================

class Student:

    def __init__(self):
        self.__grade = "A"


s = Student()

# This does NOT modify the original private-ish variable:

s.__grade = "B"


# Instead, Python creates a NEW attribute:
#
# _Student__grade -> "A"   <- original
# __grade         -> "B"   <- new attribute


print(s.__grade)             # B

# Original private-ish variable is still:

print(s._Student__grade)    # A


# ============================================================
# WHY DOES s.__grade = "B" NOT GIVE AN ERROR?
# ============================================================

# This is VERY important.
#
# Assignment can create a new attribute if it doesn't exist.
#
# So:
#
# s.__grade = "B"
#
# means:
#
# "Create/change an attribute called __grade."
#
# It does NOT mean:
#
# "Change _Student__grade."
#
#
# But if we try to READ an attribute that doesn't exist:
#
# print(s.something)
#
# Python gives:
#
# AttributeError
#
#
# Example:
#
# s = Student()
# print(s.__grade)
#
# If __grade was never created outside the class,
# this gives AttributeError.


# ============================================================
# 7. ENCAPSULATION USING NORMAL GETTER AND SETTER METHODS
# ============================================================

class Person:

    def __init__(self, age):
        self.__age = age

    # Getter
    def get_age(self):
        return self.__age

    # Setter
    def set_age(self, age):

        if age >= 0 and age <= 120:
            self.__age = age
        else:
            print("Invalid age")

    # Display
    def display(self):
        print(f"AGE: {self.__age}")


p = Person(25)

p.display()

# Change age using setter
p.set_age(30)

# Read age using getter
print(p.get_age())

# Invalid age
p.set_age(-5)


# ============================================================
# 8. GETTER
# ============================================================

# Getter means:
#
# A method used to READ/access private data.


class Person:

    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


p = Person(30)

print(p.get_age())


# ============================================================
# 9. SETTER
# ============================================================

# Setter means:
#
# A method used to CHANGE/UPDATE private data.


class Person:

    def __init__(self, age):
        self.__age = age

    def set_age(self, age):

        if age >= 0 and age <= 120:
            self.__age = age
        else:
            print("Invalid age")


p = Person(30)

p.set_age(40)


# ============================================================
# 10. PROPERTY
# ============================================================

# @property is the Pythonic way of creating a getter.
#
# It allows us to use a method like an attribute.
#
# Normal method:
#
# p.get_age()
#
# Property:
#
# p.age
#
# We do NOT use parentheses with a property.


class Person:

    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        # Getter
        return self.__age


per = Person(30)

print(per.age)

# NOT:
#
# print(per.age())
#
# because age is a property, not a normal method.


# ============================================================
# 11. PROPERTY WITH GETTER AND SETTER
# ============================================================

class Person:

    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        # Getter
        return self.__age

    @age.setter
    def age(self, value):
        # Setter
        self.__age = value


per = Person(30)

# Getter
print(per.age)

# Setter
per.age = 40

# Getter again
print(per.age)


# ============================================================
# 12. PROPERTY WITH VALIDATION
# ============================================================

# The real power of a setter is that we can validate data
# before changing the private variable.


class Person:

    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):

        if value >= 0 and value <= 120:
            self.__age = value
        else:
            print("Invalid age")


per = Person(30)

print(per.age)

per.age = 40
print(per.age)

per.age = -5
# Invalid age

print(per.age)
# Still 40


# ============================================================
# 13. BOOK EXAMPLE
# ============================================================

class Book:

    def __init__(self, author):
        self.__author = author

    @property
    def name(self):
        # Getter
        return self.__author

    @name.setter
    def name(self, newname):
        # Setter
        self.__author = newname


b = Book("Goutham")


# Getter
print(b.name)
# Goutham


# Setter
b.name = "Nandhu"


# Getter
print(b.name)
# Nandhu


# IMPORTANT:
#
# Because the setter is:
#
# @name.setter
# def name(...)
#
# we use:
#
# b.name = "Nandhu"
#
# NOT:
#
# b.changename = "Nandhu"
#
# There is no changename property in this class.


# ============================================================
# 14. WHAT HAPPENS WITH b.__author?
# ============================================================

b = Book("Goutham")

# This creates a NEW attribute.
#
# It does NOT change the original private-ish variable.

b.__author = "kjkk"


print(b.__author)
# kjkk


print(b.name)
# Goutham


# Why?
#
# Original:
#
# _Book__author -> "Goutham"
#
# New attribute:
#
# __author -> "kjkk"
#
# They are TWO DIFFERENT attributes.


# ============================================================
# 15. PROVING THE TWO ATTRIBUTES
# ============================================================

print(b.__dict__)

# You will see something similar to:
#
# {
#     '_Book__author': 'Goutham',
#     '__author': 'kjkk'
# }


# ============================================================
# 16. INSIDE CLASS vs OUTSIDE CLASS
# ============================================================

class Book:

    def __init__(self, author):
        self.__author = author

    def change_author(self, new_author):

        # INSIDE CLASS
        #
        # self.__author
        #
        # becomes:
        #
        # self._Book__author

        self.__author = new_author


b = Book("Goutham")

# Change through method
b.change_author("Nandhu")


# Original private variable changed
#
# _Book__author -> "Nandhu"


# ============================================================
# 17. OUTSIDE CLASS ACCESS
# ============================================================

b.__author = "Kiran"

# This creates:
#
# __author -> "Kiran"
#
# It does NOT change:
#
# _Book__author -> "Nandhu"


print(b.__author)          # Kiran
print(b.name if hasattr(b, "name") else "No name")


# ============================================================
# 18. THE COMPLETE ENCAPSULATION FLOW
# ============================================================

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    # Getter
    @property
    def balance(self):
        return self.__balance

    # Setter
    @balance.setter
    def balance(self, amount):

        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")


account = BankAccount(1000)

# GET
print(account.balance)
# 1000

# SET
account.balance = 1500

# GET again
print(account.balance)
# 1500

# Invalid SET
account.balance = -500
# Balance cannot be negative

print(account.balance)
# 1500


# ============================================================
# 19. PUBLIC / PROTECTED / PRIVATE SUMMARY
# ============================================================

# PUBLIC
#
# self.name
#
# Can be accessed normally.
#
# Example:
#
# obj.name


# PROTECTED
#
# self._name
#
# Convention only.
#
# Means:
# "Intended for internal/subclass use."
#
# Python still allows:
#
# obj._name


# PRIVATE-ISH
#
# self.__name
#
# Name mangling occurs:
#
# self.__name
#
# becomes approximately:
#
# self._ClassName__name
#
# Example:
#
# self.__grade
#
# becomes:
#
# self._Student__grade


# ============================================================
# 20. ATTRIBUTE ERROR
# ============================================================

# AttributeError usually happens when we TRY TO READ
# an attribute that does not exist.


class Example:

    def __init__(self):
        self.__value = 10


e = Example()

# This does not exist outside the class:

# print(e.__value)
#
# ❌ AttributeError


# But assignment can create a new attribute:

e.__value = 20

# Now __value exists as a separate outside attribute.

print(e.__value)
# 20


# Original private-ish attribute is still:

print(e._Example__value)
# 10


# ============================================================
# 21. PASS
# ============================================================

# pass means:
#
# "Do nothing."
#
# It is used when a block is intentionally empty.


class EmptyClass:
    pass


def future_function():
    pass


class Student:

    def __init__(self):
        pass


# pass does NOT mean:
# "exit the function"
#
# pass simply does nothing.


# return means:
#
# "Leave the function."


def example1():
    pass


def example2():
    return


def example3():
    return 10


# ============================================================
# 22. FINAL CHEAT SHEET
# ============================================================

# ENCAPSULATION
#
# Controlling access to an object's internal data.
#
#
# PUBLIC
# name
#       ↓
# Directly accessible
#
#
# PROTECTED
# _name
#       ↓
# Convention
# "Don't access directly"
#
#
# PRIVATE-ISH
# __name
#       ↓
# Name mangling
# _ClassName__name
#
#
# GETTER
#       ↓
# Used to READ private data
#
# @property
# def age(self):
#     return self.__age
#
#
# SETTER
#       ↓
# Used to CHANGE private data
#
# @age.setter
# def age(self, value):
#     self.__age = value
#
#
# NAME MANGLING
#
# __age
#   ↓
# _Person__age
#
#
# INSIDE CLASS
#
# self.__age
#   ↓
# _ClassName__age
#
#
# OUTSIDE CLASS
#
# obj.__age
#   ↓
# Looks for literal "__age"
#
# If it doesn't exist:
# AttributeError
#
#
# BUT:
#
# obj.__age = 50
#
# can create a NEW attribute.
#
#
# PASS
#   ↓
# Do nothing
# Used for intentionally empty blocks.
#
#
# ============================================================
# MOST IMPORTANT EXAMPLE TO REMEMBER
# ============================================================

class Person:

    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        # GETTER
        return self.__age

    @age.setter
    def age(self, value):
        # SETTER
        if 0 <= value <= 120:
            self.__age = value
        else:
            print("Invalid age")


p = Person(25)

print(p.age)        # GET -> 25

p.age = 30          # SET -> changes __age

print(p.age)        # GET -> 30

# Don't directly access:
#
# p.__age
#
# because __age was name-mangled to:
#
# _Person__age
#
# Direct assignment:
#
# p.__age = 50
#
# creates a NEW attribute; it does not change
# the original _Person__age.


class Garudan:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        self.__age+=value

a=Garudan('goutham',23)
print(a.__age)
a.age=80
a.__age=990 
print(a.__dict__)