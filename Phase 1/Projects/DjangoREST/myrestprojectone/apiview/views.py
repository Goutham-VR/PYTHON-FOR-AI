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
    # GET
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
    #PUT
    def put(self,request,id):
        dbdata=get_object_or_404(Book,id=id)
        serializer=BookSerialiser(dbdata,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class BookManageView(APIView): # class
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

# DRF GenericAPIView
# The main reason for GenericAPIView is simple:
# APIView gives us HTTP methods. GenericAPIView gives us reusable database/serializer functionality so we write less repeated code.
# GenericAPIView alone does NOT automatically provide GET/POST/PUT/DELETE. So we normally combine GenericAPIView with mixins.

# What are Mixins?
# Mixins are ready-made classes that provide common operations.

# 1. ListModelMixin -> List objects
# 2. CreateModelMixin -> Create object
# 3. RetrieveModelMixin -> Get one object
# 4. UpdateModelMixin -> Update object
# 5. DestroyModelMixin -> Delete object

# Think of them as pre-written CRUD functionality.

# Import
from rest_framework.generics import GenericAPIView # For 

class ProductListView(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer