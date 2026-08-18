from django.urls import path
from api import views

urlpatterns=[
    #Basic API Requests
    path('hello/',views.hello), #GET retrieve data.
    path('student/',views.student), #POST send json data to the server.
    path('officer/',views.officer), #POST send json data to the server and print each data.
    path('getpost/',views.getpost), #Let's make one API that accepts both GET and POST.
    path('customfun/',views.customfun), #GET with some async method.

    #CURD Operation
    path('create/',views.create), #POST Create/Insert to table
    path('getdata/<int:id>/',views.getdata), #GET Select data from table
    path('deletedata/<int:id>/',views.deletedata), #DELETE delete data from db using PK
    path('updatedata/<int:id>/',views.updatedata), #PUT update data from db using PK
]