from django.urls import path
from AuthApp import views

urlpatterns=[
    # Authentication
    path('EmployeeListViewApiSA/',views.EmployeeListViewSA.as_view()), # Session Authentication - session id based
    path('EmployeeListViewApiBA/',views.EmployeeListViewBA.as_view()), # Basic Authentication - every time need username and password for request
    path('EmployeeListViewApiTA/',views.EmployeeListViewTA.as_view()), # Token Authentication - Login once with username & password -> generate token -> Every API request uses the token

    # Permission - built-in
    path('EmployeeListViewApiPermissionSA/',views.EmployeeListViewApiPermissionSA.as_view()),
    # BA
    # TA
    
    # Permission - custom

]