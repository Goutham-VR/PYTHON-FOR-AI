from django.db import models

# Create your models here.
class ProductTwo(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    order_date = models.DateField()