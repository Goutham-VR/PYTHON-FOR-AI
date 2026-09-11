from django.shortcuts import render

# Create your views here.

# We already know about APIView/GenericAPIView/ConcreteGenericAPIView othervise check apiview app
# Create a pagination class in a file called pagination.py inside your API app:

# ==================import for serializers==============================
from PaginationApiView.serializers import ProductSerializer
# ======================================================================

# ==================import for Models===================================
from apiview.models import Product
# ======================================================================

# ================import for pagination====================
from PaginationApiView.pagination import ProductPagination
from PaginationApiView.pagination import ProductLimitPagination
from PaginationApiView.pagination import ProductCursorPagination
#==========================================================

# ================import for ====================
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView

# Concrete Generic APi View
#===================class for insert Products===========================
class AddProductConcrete(CreateAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    # no pagination class here becaouse its a POST/create view

#===================class for select with pagenumber pagination====================================
class ProductListViewPN(ListAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    pagination_class=ProductPagination # Type 1 pagination

#===================class for select with limit offset pagination====================================
class ProductListViewLO(ListAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    pagination_class=ProductLimitPagination # Type 2 Pagination

class ProductListViewCursorPagination(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductCursorPagination