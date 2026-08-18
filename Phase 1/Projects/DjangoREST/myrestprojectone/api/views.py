from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Student

import asyncio
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

@api_view(['GET'])
def customfun(request):
    async def task1():
        print("Task 1 Start")
        await asyncio.sleep(5)
        print("Task 1 End")
    async def task2():
        print("Task 2 Start")
        await asyncio.sleep(2)
        print("Task 2 End")
    async def main():
        await asyncio.gather(task1(),task2())

    asyncio.run(main())
    return Response({
        'message':"Task Finished"
    })

@api_view(['POST'])
def create(request):
    Student.objects.create(name=request.data['name'],
                           age=request.data['age'],
                           course=request.data['course'])
    return Response({
        'message':'Data Inserted'
    })

@api_view(['GET'])
def getdata(request,id):
    dbdata=Student.objects.get(id=id)
    Name=dbdata.name
    Age=dbdata.age
    Course=dbdata.course
    return Response({
        'message':'Data Retrieved',
        'Name':Name,
        'Age':Age,
        'Course':Course
    })

@api_view(['DELETE'])
def deletedata(request,id):
    Student.objects.get(id=id).delete()
    return Response({
        'message':"Data Deleted"
    })

@api_view(['PUT'])
def updatedata(request,id):
    dbdata=Student.objects.get(id=id)
    dbdata.name=request.data['name']
    dbdata.age=request.data['age']
    dbdata.course=request.data['course']
    dbdata.save()
    return Response({
            'message':"Data Updated"
    })