from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import APIView  # Class Based api views
# from rest_framework.decorators import api_view # this is for function Based api views, Not needed Here 

# Concept 1: API View : APIView allows us to convert that function into a class.
# if request.method == 'GET': change to def get(self, request):
# if request.method == 'POST': change to def post(self, request):

# FBV                         APIView
# request.method == GET   →   get()
# request.method == POST  →   post()
# request.method == PUT   →   put()
# request.method == PATCH →   patch()
# request.method == DELETE→   delete()

# Model Import
from apiview.models import Book
from apiview.models import Product

# Serializer Import
from apiview.serializers import BookSerialiser
from apiview.serializers import ProductSerializer

# Create your views here.
class BookListAPIView(APIView): # class
    # GET All
    def get(self,request): # method 1
        dbdata=Book.objects.all()
        serializer=BookSerialiser(dbdata,many=True)
        return Response(serializer.data)

    # POST
    def post(self,request): # method 2
        serializer=BookSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class BookManageView(APIView): # class
    # GET ONE
    def get(self,request,id): # method 1
        dbdata=get_object_or_404(Book,id=id)
        serializer=BookSerialiser(dbdata)
        return Response(serializer.data)
    #PUT
    def put(self,request,id):
        dbdata=get_object_or_404(Book,id=id)
        serializer=BookSerialiser(dbdata,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    #PATCH
    def patch(self,request,id):
        dbdata=get_object_or_404(Book,id=id)
        serializer=BookSerialiser(dbdata,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    #DELETE
    def delete(self,request,id):
        dbdata=get_object_or_404(Book,id=id)
        dbdata.delete()
        return Response({'message':'Data Deleted'})
    
# =================================================================================================================================
# DRF GenericAPIView
#==================================================================================================================================
# The main reason for GenericAPIView is simple:
# APIView gives us HTTP methods. GenericAPIView gives us reusable database/serializer functionality so we write less repeated code.
# GenericAPIView alone does NOT automatically provide GET/POST/PUT/DELETE. So we normally combine GenericAPIView with mixins.

# What are Mixins?
# Mixins are ready-made classes that provide common operations.

# 1. ListModelMixin -> List objects : self.list()
# 2. CreateModelMixin -> Create object : self.create()
# 3. RetrieveModelMixin -> Get one object : self.retrieve()
# 4. UpdateModelMixin -> Update object : self.update()/self.partial_update()
# 5. DestroyModelMixin -> Delete object : self.destroy()

# Think of them as pre-written CRUD functionality.

# eg structre:

# class classname(mixin_name,GenericAPIView):
#     queryset=tablename.objects..........
#     serializer_class=serializername

#     def get(self,request): 
#         return self.mixin_function(request)

# Import libs
from rest_framework.generics import GenericAPIView # For Generic APIview
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class ProductListView(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    #GET ALL
    def get(self,request):
        return self.list(request)
    #POST
    def post(self,request):
        return self.create(request)

class ProductDetailView(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_url_kwarg = 'id' # if we want url parameter name
    #GET ONE
    def get(self,request,pk):
        return self.retrieve(request,pk=pk)
    #PUT
    def put(self,request,pk):
        return self.update(request,pk=pk)
    #PATCH
    def patch(self,request,pk):
        return self.partial_update(request,pk=pk)
    #DELETE
    def delete(self,request,pk):
        return self.destroy(request,pk=pk)

# Generic view with message
class ProductList(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    #GET All
    def get(self,request):
        response = self.list(request)
        response.data = {
            'message':'Products Retrieved',
            'data':response.data
        }
        return response
    #POST
    def post(self,request):
        response = self.create(request)
        response.data = {
            'message':'Product Inserted',
            'data':response.data
        }
        return response

class ProductManager(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    #GET One
    def get(self,request,pk):
        response=self.retrieve(request,pk=pk)
        response.data={
            'message':'Product Retrived',
            'data':response.data
        }
        return response
    #PUT
    def put(self,request,pk):
        response=self.update(request,pk=pk)
        response.data={
            'message':'Product Updated',
            'data':response.data
        }
        return response
    #PATCH
    def patch(self,request,pk):
        response=self.partial_update(request,pk=pk)
        response.data={
            'message':'Product Patched',
            'data':response.data
        }
        return response
    #DELETE
    def delete(self,request,pk):
        response=self.destroy(request,pk=pk)
        response.data={
            'message':'Product Deleted',
            'data':response.data
        }
        return response
    
# ==================================================================================================================
# Concrete Generic APIViews
# ==================================================================================================================
# it automatically handle methods like get post put patch delete. so we dont write methods
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class ConcreteListCreateProduct(ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ConcreteRUPDProduct(RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

#==============================================================================================================
# Individual Concrete Generic APIView
#==============================================================================================================
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView

class ConcreteListProduct(ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ConcreteRetrieveProduct(RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ConcreteCreateProduct(CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ConcreteUpdateProduct(UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ConcreteDestroyProduct(DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

# in concrete generic view we can also override methods if we want customization

#=====================================================================================
# get_queryset() = Used to override ListAPIViews readymade listing method
#=====================================================================================
# get_queryset() belongs to GenericAPIView, so it works with the GenericAPIView family, including the Concrete Generic Views because they are built on top of GenericAPIView.

# Normal APIView
#    ❌ get_queryset() is not built-in

# GenericAPIView
#    ✅ get_queryset() works

# Concrete Generic Views
#    ✅ get_queryset() works

# get_queryset() is especially useful for: Filtering, User-specific data, URL-based filtering, Query parameters, Permissions-related data selection
# so queryset = Simple/static data and get_queryset() = Dynamic/custom data
# Eg:
class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.filter(price__gt=1000)

#=====================================================================================
# get_object() = Used to override RetrieveAPIViews readymade get one method
#=====================================================================================
# get one object
class ProductDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    def get_object(self):
        return Product.objects.get(pk=self.kwargs['pk'],price__gt=1000)

#=====================================================================================
# lookup_field  = override default pk with other field
#=====================================================================================
# get one object using model field
# Normally DRF finds an object using its primary key.With lookup_field, you can tell DRF to use another model field instead.
# lookup_field = which model field should DRF search?
class ConcreteRetrieveProduct(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'name' # use model field name also equal to url parameter eg <str:name>

#=====================================================================================
# lookup_url_kwarg
#=====================================================================================
# lookup_url_kwarg = which URL parameter should DRF read?
# suppose:
# path('products/<str/product_name>/', views.ConcreteRetrieveProduct.as_view())
# Here the URL parameter is: product_name
# But our model field is:name
# So we can write:

class ConcreteRetrieveProduct(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'name' # use model field name
    lookup_url_kwarg = 'product_name' # use url parameter name eg <str:product_name>

#=====================================================================================
# perform_create()
#=====================================================================================
# This is used when you want to customize what happens when a new object is created.
# You can use it with:
#     1. CreateAPIView
#     2. ListCreateAPIView
#     3. CreateModelMixin

from rest_framework.generics import CreateAPIView
class ConcreteInsertProduct(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        serializer.save()

#=====================================================================================
# perform_update()
#=====================================================================================
# perform_update() is used when you want to customize what happens when an existing object is updated.
# Suppose you want to automatically change the category whenever a product is updated:
# You can use it with:
#     1. UpdateAPIView
#     2. RetrieveUpdateDestroyAPIView
#     3. UpdateModelMixin

class UpdateProduct(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_update(self, serializer):
        serializer.save(category="Updated")

#=====================================================================================
# perform_destroy()
#=====================================================================================
# perform_destroy() is used when you want to customize what happens when an object is deleted.
# It is mainly used with:
#     1. DestroyAPIView
#     2. RetrieveUpdateDestroyAPIView
#     3 .DestroyModelMixin

class DeleteProduct(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_destroy(self, instance):
        print("Deleting:", instance.name)
        instance.delete()
