from django.urls import path
from api import views

urlpatterns=[
    path('hello/',views.hello), #GET retrieve data.
    path('student/',views.student), #POST send json data to the server.
    path('officer/',views.officer), #POST send json data to the server and print each data.
    path('getpost/',views.getpost), #Let's make one API that accepts both GET and POST.
]