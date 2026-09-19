from django.urls import path
from FilteringAPIView import views

# Important Concept:
#1. /ProductListView/?category=Mobile : use self.request.query_params.get('category') in view
#2. /ProductListView/Mobile/  : use self.kwarg.get('category')

urlpatterns=[
    path('ProductListViewQueryParam/',views.ProductListViewQueryParam.as_view()), # self.request.query_params.get('category') in views if use this. Then the client can add query parameters after ?
    path('ProductListViewKWARGS/<str:category>/',views.ProductListViewKWARGS.as_view()), # self.kwarg.get('category') in views if use this
    path('ProductListViewDjangoFilter/',views.ProductListViewDjangoFilter.as_view()), # here using django filter
]