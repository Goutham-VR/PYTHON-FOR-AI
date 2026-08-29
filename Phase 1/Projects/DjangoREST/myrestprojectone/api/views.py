from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

#importing models
from api.models import Student
from api.models import Computer

#importing Serializers
from api.serializers import StudentSerializer
from api.serializers import StudentSerializerWithFieldRule
from api.serializers import StudentCreateUpdateserializerwithvalidation

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

#Starts with Serializer Concept
#serializer get
@api_view(['GET'])
def sget(request,id):
    dbdata=Student.objects.get(id=id)
    serializer=StudentSerializer(dbdata) # modal to json serializing format
    return Response({
        'message':'Data Retrieved',
        'data':serializer.data}
    )

#serializer create
@api_view(['POST'])
def screate(request):
    serializer=StudentSerializer(data=request.data) # json to Serializer serializing format
    if serializer.is_valid():
        serializer.save()

        return Response({
            'message':'Data Inserted',
            'data':serializer.data
        })
    return Response(serializer.errors)

# serializer PUT and PATCH
# PUT — complete update = edit ful
@api_view(['PUT'])
def supdatestudent(request,id):
    dbdata=Student.objects.get(id=id)
    serializer=StudentSerializer(dbdata,data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response({
            'message':"Data Updated",
            'data':serializer.data
        })
    return Response(serializer.errors)

# PATCH — partial update = edit partial
@api_view(['PATCH'])
def supdatestudent(request,id):
    dbdata=Student.objects.get(id=id)
    serializer=StudentSerializer(dbdata,data=request.data,partial=True) # difference is the parameter - add partial = True
    if serializer.is_valid():
        serializer.save()

        return Response({
            'message':"Data Updated",
            'data':serializer.data
        })
    return Response(serializer.errors)
    
# serializer with bultin and custom rules/field validation eg
@api_view(['POST'])
def createstudentsbc(request):
    serializer=StudentSerializerWithFieldRule(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response({
            'message':'Data Inserted',
            'data':serializer.data
        })
    return Response(serializer.errors)

@api_view(['GET'])
def getstudentsbc(request,id):
    dbdata=Student.objects.get(id=id)
    serializer=StudentSerializerWithFieldRule(dbdata)
    return Response({
        'message':"Data Retrieved",
        'data':serializer.data
    })

@api_view(['PUT'])
def putstudentsbc(request,id):
    dbdata=Student.objects.get(id=id)
    serializer=StudentSerializerWithFieldRule(dbdata,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':"Data Updated",
            'data':serializer.data
        })
    return Response(serializer.errors)

@api_view(['PATCH'])
def patchstudentsbc(request,id):
    dbdata=Student.objects.get(id=id)
    serializer=StudentSerializerWithFieldRule(dbdata,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':"Data Updated",
            'data':serializer.data
        })
    return Response(serializer.errors)

# Using Serializer with create and update method and builtin/custom validation
@api_view(['POST'])
def createstudentcmv(request):
    serializer=StudentCreateUpdateserializerwithvalidation(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':"Data Inserted",
            'data':serializer.data
        })
    return Response(serializer.errors)

@api_view(['GET'])
def getstudentcmv(request,id):
    dbdata=Student.objects.get(id=id)
    serializer=StudentCreateUpdateserializerwithvalidation(dbdata)
    return Response({
        'message':'Data Retrieved',
        'data':serializer.data
    })

@api_view(['PUT'])
def putstudentcmv(request,id):
    dbdata=Student.objects.get(id=id)
    serializer=StudentCreateUpdateserializerwithvalidation(dbdata,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':'Data Updated',
            'data':serializer.data
        })
    return Response(serializer.errors)

@api_view(['PATCH'])
def patchstudentcmv(request,id):
    dbdata=Student.objects.get(id=id)
    serializer=StudentCreateUpdateserializerwithvalidation(dbdata,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':'Data Pathed',
            'data':serializer.data
        })