import django_filters
from apiview.models import Product

class ProductFilter(django_filters.FilterSet): # "Create a filter configuration for my Product model."
    class Meta:
        model=Product # Model Name For Filter
        fields=['category'] # "I want users to filter Products using the category field." [] for fields is mandatory here not like serializers