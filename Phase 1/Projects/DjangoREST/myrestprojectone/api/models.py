from django.db import models

# Create your models here.

# Start With Model and Serializer
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    course=models.CharField(max_length=100)
    def __str__(self):
        return self.name

# Created For Test Purpose
class Computer(models.Model):
    processor=models.CharField(max_length=100)
    ram=models.IntegerField()
    def __str__(self):
        return self.processor

# Created for Nested Serializers
class Department(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.name