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
    
    # Permission - custom - has_permission()
    path('CourseListViewApiCustomPermissionSA/',views.CourseListView.as_view()), # List
    path('CourseListViewTwoApiCustomPermissionSA/',views.CourseListView.as_view()), # List
    path('NotesCreateViewApiCustomPermissionSA/',views.NotesCreateView.as_view()), # Create

    # Permission - custom - has_object_permission()
    path('NotesGetOneAPIViewCustomPermissionSA/<int:pk>/',views.NotesGetOneAPIView.as_view()), # List Get One
    path('NotesGetAllAPIViewCustomPermissionSA/',views.NotesGetAllAPIView.as_view()), # List filter based on user auth
    path('NotesUpdateAPIViewCustomPermissionSA/<int:pk>/',views.NotesUpdateAPIView.as_view()), # Update based on user auth works for PUT and PATCH

]