from django.urls import path
from SearchAPIView import views

urlpatterns=[
    path('CourseSearchFilterListView/',views.CourseSearchFilterListView.as_view()),
    path('CourseOrderingListView/',views.CourseOrderingListView.as_view()),
]