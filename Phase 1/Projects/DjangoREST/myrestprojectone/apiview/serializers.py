from rest_framework import serializers
from apiview.models import Book
from apiview.models import Product

# creating simple serializer
class BookSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'