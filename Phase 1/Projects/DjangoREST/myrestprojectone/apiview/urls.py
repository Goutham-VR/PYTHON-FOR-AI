from django.urls import path
from apiview import views

urlpatterns=[
    # Normal APIView
    path('books/',views.BookListAPIView.as_view()),
    path('booksmanage/<int:id>/',views.BookManageView.as_view()),

    # Generic APIView
    
]