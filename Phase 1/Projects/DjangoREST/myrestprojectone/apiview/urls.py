from django.urls import path
from apiview import views

urlpatterns=[
    # 1. Normal APIView
    #==================
    path('books/',views.BookListAPIView.as_view()), # GET All, POST
    path('booksmanage/<int:id>/',views.BookManageView.as_view()), # GET One,PUT,PATCH,DELETE

    # 2. Generic APIView
    # ==================
    path('ProductListViewGeneric/',views.ProductListView.as_view()), # GET All, POST
    path('ProductDetailViewGeneric/<int:pk>/',views.ProductDetailView.as_view()), # GET One,PUT,PATCH,DELETE 
    # For Generic view use pk instead of id. if u need id mention it in the class eg: lookup_url_kwarg = 'id'

    # Pass Message with data in Generic view
    path('ProductListGeneric/',views.ProductList.as_view()), # GET All, POST
    path('ProductManagerGeneric/<int:pk>/',views.ProductManager.as_view()), # GET One,PUT,PATCH,DELETE 

    # 3. Concrete Generic APIView
    # ===========================
    path('ProductListConcreteGeneric/',views.ConcreteListCreateProduct.as_view()), # GET All, POST
    path('ProductManagerConcreteGeneric/<int:pk>/',views.ConcreteRUPDProduct.as_view()), # GET One,PUT,PATCH,DELETE 

    # 3. Individual Concrete Generic APIView
    # ======================================
    path('ProductListIndividualConcreteGeneric/',views.ConcreteListProduct.as_view()), # GET All
    path('ProductManagerIndividualConcreteGeneric/',views.ConcreteCreateProduct.as_view()), # POST
    path('ProductManagerIndividualConcreteGeneric/<int:pk>/',views.ConcreteRetrieveProduct.as_view()), # GET One
    path('ProductManagerIndividualConcreteGeneric/<int:pk>/',views.ConcreteUpdateProduct.as_view()), # PUT,PATCH 
    path('ProductManagerIndividualConcreteGeneric/<int:pk>/',views.ConcreteDestroyProduct.as_view()), # DELETE 

]