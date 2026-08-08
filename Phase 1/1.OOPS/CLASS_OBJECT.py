class Laptop:
    def __init__(self,brand,ram,storage):
        self.brand=brand
        self.ram=ram
        self.storage=storage

    def display(self):
        print(f" BRAND:{self.brand}")
        print(f" RAM:{self.ram}")
        print(f" STORAGE:{self.storage}")

data= Laptop("Lenovo","4GB","128GB")
data.display()

class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposite(self,amount):
        self.balance=self.balance+amount
        return self.balance
    
    def withdraw(self,amount):
        self.balance=self.balance-amount
        return self.balance

    def display(self):
        print(f" OWNER:{self.owner}")
        print(f" Balance:{self.balance}")

acc=BankAccount("John",5000)
acc.deposite(1000)
acc.withdraw(700)
acc.display()

class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length

    def area(self):
        w=self.width
        l=self.length
        return l*w

    def peri(self):
        w=self.width
        l=self.length
        return 2*(l+w)

r=Rectangle(10,5)
print(r.area())
print(r.peri())

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def increase_salary(self,percent):
        incriment=(percent/100)*self.salary
        self.salary=self.salary+incriment
        return self.salary

    def display(self):
        print(f" Employee:{self.name}")
        print(f" Salary:{self.salary}")

emp=Employee("Alice",50000)
emp.increase_salary(10)
emp.display()