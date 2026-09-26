from django.shortcuts import render
from FilteringAPIView.serializers import ProductSerializer
from rest_framework.generics import ListAPIView
from apiview.models import Product

# Create your views here.

#==========================================================================================================================
# FILTERING USING GET_QUERYSET() : This method is already done in previous section
#==========================================================================================================================
# 1. Filtering Using Query Params commonly used for Searching and filtering 
class ProductListViewQueryParam(ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        category = self.request.query_params.get('category') # reads values after ?. parameter is considered by client 
        return Product.objects.filter(category=category)

# 2. Use kwargs.get() for URL parameters: we pass parameter like this in url = <str:category>/<datatype:value>
class ProductListViewKWARGS(ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        category = self.kwargs.get('category')
        return Product.objects.filter(category=category)

# 3. Use if You already have the user from authentication like session/basic/token/jwt: request.user = logged in user
class MyProductListView(ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)

#==========================================================================================================================
# DJANGO-FILTER - Proper DRF Filtering
#==========================================================================================================================
# API has many filters, writing everything inside get_queryset() becomes messy so DRF commonly uses the django-filter package for this.
# step 1 : pip install django filter
# step 2 : add 'django-filters' to apps in settings.py
# step 3 : add in settings
#         REST_FRAMEWORK = {
#             'DEFAULT_FILTER_BACKENDS': [
#                 'django_filters.rest_framework.DjangoFilterBackend',
#             ],
#         }
# step 4 : create filters.py and add code
# step 5 : APIview for filter

from django_filters.rest_framework import DjangoFilterBackend
from FilteringAPIView.filters import ProductFilter

class ProductListViewDjangoFilter(ListAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend] # New Concept for Filter
    filterset_class = ProductFilter # New concept for calling filter from filters.py