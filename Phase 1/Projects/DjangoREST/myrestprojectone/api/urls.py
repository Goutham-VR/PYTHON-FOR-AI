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
    
    #CURD with Serializer Eg 1
    path('sget/<int:id>/',views.sget), #GET Select data from table with serializer
    path('screate/',views.screate), #POST Create/Insert to table with serializer
    path('supdatestudent/<int:id>/',views.supdatestudent),
    # path('deleet')

    # CURD - Serializer with built-in and custom rule/field validation
    path('createstudentsbc/',views.createstudentsbc),
    path('getstudentsbc/<int:id>/',views.getstudentsbc),
    path('putstudentsbc/<int:id>/',views.putstudentsbc),
    path('patchstudentsbc/<int:id>/',views.patchstudentsbc),
    # delete

    # CURD - Serializer with create and update method & all-type validation
    path('createstudentcmv/',views.createstudentcmv),
    path('getstudentcmv/<int:id>/',views.getstudentcmv),
    path('putstudentcmv/<int:id>/',views.putstudentcmv),
    path('patchstudentcmv/<int:id>/',views.patchstudentcmv),
]