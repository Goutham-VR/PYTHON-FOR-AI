from django.urls import path
from PaginationApiView import views

urlpatterns=[
    path('AddProductConcrete/',views.AddProductConcrete.as_view()),
    path('ProductListViewPagenumber/',views.ProductListViewPN.as_view()),
    path('ProductListViewLimitOffset/',views.ProductListViewLO.as_view()),
    path('ProductListViewCursor/',views.ProductListViewCursorPagination.as_view()),
    
]