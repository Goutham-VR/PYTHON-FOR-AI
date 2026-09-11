#=========================================================================================
# Pagination - real-world DRF feature.
#=========================================================================================
# Imagine your database has: 100,000 Products
# Returning all 100,000 objects in one response is inefficient.
# Instead, we divide them into pages:
#     Page 1 → Products 1–10
#     Page 2 → Products 11–20
#     Page 3 → Products 21–30
#     ...
# This is called pagination.

# This is configured in settings.py - check for below lines in settings
# REST_FRAMEWORK = { pagination codes.....  }

# Steps
# 1. Create a pagination class
# 2. Connect it to ProductListView

from rest_framework.pagination import PageNumberPagination
class ProductPagination(PageNumberPagination):
    page_size = 5 # By default, each page contains 5 products.
    page_size_query_param = 'page_size' # The client can request a different number:
    max_page_size = 20 # Even if someone requests: /products/?page_size=1000 DRF won't allow more than 20.


from rest_framework.pagination import LimitOffsetPagination
class ProductLimitPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 20

from rest_framework.pagination import CursorPagination
class ProductCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'id'