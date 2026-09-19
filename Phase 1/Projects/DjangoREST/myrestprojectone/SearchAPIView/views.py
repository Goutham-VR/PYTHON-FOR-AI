
#================================================================================
# SearchFilter 
#================================================================================
# SearchFilter is useful when the user doesn't know the exact value they want and simply wants to search
# SearchFilter Used for text searching:
# Used for text searching: ?search=python
# if description = "Learn anypython programming"
# then python matches because the text occurs inside the field.
# No. SearchFilter does not need a separate filter.py file.
# For django-filter, we created filters.py because we were defining a FilterSet:

# DjangoFilterBackend → structured filtering
# You specify a field and condition.
# ?price__gte=50000
# ?category=Mobile

# SearchFilter → text-based / less-structured searching
# ?search=python
# name        → "Python Basics"
# description → "Learn anypython programming"
# category    → "Programming"

from django.shortcuts import render

from SearchAPIView.serializers import CourseSerializer # import Serializer
from SearchAPIView.models import Course # import models

from rest_framework.filters import SearchFilter # import search filter
from rest_framework.generics import ListAPIView # import API View

# Basic Search Concrete Generic APiView
class CourseSearchFilterListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    filter_backends = [SearchFilter]
    search_fields = ['name', 'description', 'category'] # search fields options
    # search_fields = ['department__name'] # search related fields (FK)

# Eg url:
# http://127.0.0.1:8000/SearchAPIView/CourseSearchFilterListView/?search=python

# search search_fields with Related Models

#================================================================================
# OrderingFilter
#================================================================================
# Course             Price
# -------------------------
# Python             5000
# Django             3000
# React              4000

# You may want:
# Lowest price → highest price

# or:
# Highest price → lowest price
# That's what OrderingFilter does.

from rest_framework.filters import OrderingFilter

class CourseOrderingListView(ListAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

    filter_backends=[OrderingFilter]
    ordering_fields = ['name', 'price', 'category']

# ordering_fields → allowed fields
# ordering        → selected field

# URL eg:
# ?ordering=price = Sort by price in ascending order.
# ?ordering=-price = The - means descending.

#================================================================================
# Combining Filter + Search + Ordering
#================================================================================
from django_filters.rest_framework import DjangoFilterBackend # import for django filter
from rest_framework.filters import SearchFilter, OrderingFilter # import serach and ordering filter
from SearchAPIView.serializers import ProductSerializer # import serializer
from apiview.models import Product  # import model form old app apiview
from FilteringAPIView.filters import ProductFilter # import product filter from filteringapiview app if need another in same app then create one in searchapiview app

class ProductListView(ListAPIView):
    queryset = Product.objects.all() #define model
    serializer_class = ProductSerializer # define serializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter] # define all imported filter
    filterset_class = ProductFilter # define filter class
    search_fields = ['name', 'category'] # add search field
    ordering_fields = ['name', 'price'] # add ordering field

#url become: apprurlname/ProductListView/?category=Mobile&search=phone&ordering=-price

# things to remember:

# django-filter
#     ?department_name=computer

# SearchFilter
#     ?search=computer

# OrderingFilter
#     ?ordering=department__name