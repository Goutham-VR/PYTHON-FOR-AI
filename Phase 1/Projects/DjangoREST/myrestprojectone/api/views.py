from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

#importing models
from api.models import Student
from api.models import Computer
from api.models import Employee
from api.models import User

#importing Serializers
# ===================NORMAL SERIALIZERS====================
from api.serializers import StudentSerializerBasic
from api.serializers import DepartmentSerializer

# ===================NORMAL SERIALIZERS WITH FIELD RULE====================
from api.serializers import StudentSerializer

# ===================SERIALIZERS WITH FIELD RULE - BUILT-IN/CUSTOM/MULTIPLE====================
from api.serializers import StudentSerializerWithFieldRule

# ===================SERIALIZERS WITH CREATE/UPDATE METHOD AND FIELD RULE====================
from api.serializers import StudentCreateUpdateserializerwithvalidation

# ===================SERIALIZERS WITH METHOD FIELD====================
from api.serializers import StudentSerializerMethodField

# ===================NESTED SERIALIZERS====================
from api.serializers import EmployeeNestedSerializer
from api.serializers import EmployeeWritableNestedSerializer
from api.serializers import EmployeeSerializer

# ===================SERIALIZERS WITH READ & WRITE====================
from api.serializers import UserSerializer

# ===================SERIALIZERS WITH SOURCE====================
from api.serializers import EmployeeSerializerWithSource

# ===================SERIALIZERS VS MODELSERIALIZERS====================
from api.serializers import StudentSerializerNormal # - non model
from api.serializers import StudentSerializerMS # - model based

# ===================SERIALIZERS WITH READ_ONLY_FIELDS====================
from api.serializers import StudentSerializerROF

# ===================SERIALIZERS WITH EXTRA_KWARGS====================
from api.serializers import StudentSerializerKWargs

# ===================SERIALIZERS WITH RELATIONSHIP FIELDS====================
from api.serializers import EmployeeSerializerRelationshipField

# ===================SERIALIZERS WITH CONTEXT====================
from api.serializers import StudentSerializerContext


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
# PUT — complete update = edit full
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

@api_view(['POST'])
def createstudentsmf(request):
    serializer=StudentSerializerMethodField(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':'Data Inserted',
            'data':serializer.data
        })
    return Response(serializer.errors)

#pending update for smf

# Department Views 
@api_view(['POST'])
def createdepartment(request):
    serializer=DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':'Department Created',
            'data':serializer.data
        })
    return Response(serializer.errors)

# Employee Views
# EmployeeWritableNestedSerializer POST
@api_view(['POST'])
def createemployee(request):
    serializer=EmployeeWritableNestedSerializer(data=request.data) # create nested object and create employee with that nested object
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':'Employee Created',
            'data':serializer.data
        })
    return Response(serializer.errors)

# EmployeeWritableNestedSerializer PUT
@api_view(['PUT'])
def putemployee(request,id):
    dbdata=Employee.objects.get(id=id)
    serializer=EmployeeWritableNestedSerializer(dbdata,data=request.data) # update Both Emplyee object and Nested object
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':'Employee Updated',
            'data':serializer.data
        })
    return Response(serializer.errors)

# EmployeeWritableNestedSerializer PATCH
@api_view(['PATCH'])
def patchemployee(request,id):
    dbdata=Employee.objects.get(id=id)
    serializer=EmployeeWritableNestedSerializer(dbdata,data=request.data,partial=True) # Patch Both Emplyee object and Nested object
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':'Employee Patched',
            'data':serializer.data
        })
    return Response(serializer.errors)

# EmployeeNestedSerializer GET
@api_view(['GET'])
def getemployee(request,id):
    dbdata=Employee.objects.get(id=id)
    serializer=EmployeeNestedSerializer(dbdata)
    return Response({
        'message':'Employee Retrieved',
        'data':serializer.data
    })

# PrimaryKeyRelatedField Serializer
@api_view(['POST'])
def createemployeeprfs(request):
    serializer=EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':'Employee Created',
            'data':serializer.data
        })
    return Response(serializer.errors)

@api_view(['PUT'])
def putemployeeprfs(request,id):
    dbdata=Employee.objects.get(id=id)
    serializer=EmployeeSerializer(dbdata,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':'Data Updated',
            'data':serializer.data
        })
    return Response(serializer.errors)

@api_view(['PATCH'])
def patchemployeeprfs(request,id):
    dbdata=Employee.objects.get(id=id)
    serializer=EmployeeSerializer(dbdata,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':'Data Patched',
            'data':serializer.data
        })
    return Response(serializer.errors)

# Read and Write Concept
# insert/POST
@api_view(['POST'])
def readwriteinsert(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':'Data Inserted',
            'data':serializer.data
        })
    return Response(serializer.errors)

# select/GET
@api_view(['GET'])
def readwriteget(request,id):
    dbdata=User.objects.get(id=id)
    serializer=UserSerializer(dbdata)
    return Response({
        'message':'Data Retrieved',
        'data':serializer.data
    })

# PUT and PATCH is same as before

# Source Concept - POST
@api_view(['POST'])
def createemployeesource(request):
    serializer=EmployeeSerializerWithSource(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':'Employee Created',
            'data':serializer.data
        })
    return Response(serializer.errors)

# Source Concept - GET
@api_view(['GET'])
def getemployeesource(request,id):
    dbdata=Employee.objects.get(id=id)
    serializer=EmployeeSerializerWithSource(dbdata)
    return Response({
        'message':'Employee Retrieved',
        'data':serializer.data
    })

# many = True Concept
# Get mutiple data many=True (Select all)
@api_view(['GET'])
def getallemployee(request):
    dbdata=Employee.objects.all()
    serializer=EmployeeSerializer(dbdata,many=True) # Use any serialiser
    return Response({
        'message':"Data Retrieved",
        'data':serializer.data
    })

# POST mutiple data many=True (Select all)
@api_view(['POST'])
def postallemployee(request):
    serializer=EmployeeSerializer(data=request.data,many=True) # Use any serialiser. input is like this: [{key:value},{key:value},{key:value}]
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':"Data Inserted",
            'data':serializer.data
        })
    return Response(serializer.errors)

# CURD for read_only_fields   - views are same, changes are in each serializers
# CURD for kwargs             - views are same, changes are in each serializers
# CURD for Relationship Field - views are same, changes are in each serializers

# CURD for Serializer Context
@api_view(['POST'])
def postserializercontext(request):
    serializer=StudentSerializerContext(context={'request':request},data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':"Data Inserted",
            'data':serializer.data
        })
    return Response(serializer.errors)