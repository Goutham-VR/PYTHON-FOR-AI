from django.urls import path
from ThrottlingApp import views

urlpatterns=[
    path('throttle/',views.ThrottlingApiView.as_view()),
    path('throttleGeneric/',views.ThrottlingGenericApiView.as_view()),
    path('throttleConcreteGeneric/',views.ThrottlingConcreteGenericApiView.as_view()),
]