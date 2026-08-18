from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(["GET"])
def hello(request):
    return Response({"message":"Hello From DRF"})

@api_view(['POST'])
def student(request):
    print(request.data)
    return Response({
        "message":"Student Data Recived",
        "data":request.data
    })

@api_view(['POST'])
def officer(request):
    print(request.data['name'])
    print(request.data['age'])
    return Response({
        'message':'Data Recived',
        'name':request.data['name'],
        'age':request.data['age']
    })

@api_view(['GET','POST'])
def getpost(request):
    if request.method=='GET':
        print('GET Done')
        return Response({
            'message':'GET Request'
        })
    if request.method=='POST':
        print('POST Done')
        return Response({
            'message':"POST Request",
            'data':request.data
        })