from rest_framework import serializers
from api.models import Student
from api.models import Department
from api.models import Employee

class StudentSerializer(serializers.ModelSerializer): #Create a serializer based on a Django model.
    class Meta:
        model=Student                                 #This serializer is connected to the Student model.
        fields='__all__'                              #Include all fields from the model.

    #adding validation for serializers
    #validate() is for multiple field validation
    #validate_fieldname() is for single field validation

    def validate_age(self,value):
        if value<18:
            raise serializers.ValidationError("Student age must be 18 or above.")
        if not isinstance(value,(int,float)):
            raise serializers.ValidationError("Student age must be Number")
        return value

    # for alphabets checking but this will fail in name like "Goutham V.R"
    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Student Name must Contains Alphabets.")
        return value

    # validate is used for multiple field validation
    def validate(self, value):
        if value['course'] == 'BCA' and value['age'] < 18:
            raise serializers.ValidationError("BCA student must be 18 or above.")
        return value


# required
# allow_blank
# allow_null
# read_only
# write_only
# default
# min_length
# max_length
# min_value
# max_value
# trim_whitespace
# These are field rule for serializer
# The rule to remember:
# If DRF's built-in validation/field rule fits your requirement perfectly → use it.
# If you have additional/custom business logic → add custom validation.

import re
class StudentSerializerWithFieldRule(serializers.ModelSerializer):

    # DRF built-in Validation/Field rule
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100,required=True,allow_blank=False,trim_whitespace=True)
    age = serializers.IntegerField(required=True,min_value=18,max_value=100)
    course = serializers.CharField(required=False,default="Degree",allow_blank=True,max_length=30)

    class Meta:
        model = Student
        fields = '__all__'

    #Custom validation rules
    def validate_name(self, value):
        if not re.fullmatch(r"[A-Za-z. ]+", value):
            raise serializers.ValidationError(
                "Name can contain only alphabets, spaces and dots."
            )
        return value

    # Custom multiple-field validation
    def validate(self, data):
        # if we send only partial data for patch data only have choosen one
        # because if we send age data contains only data['age']. checking with other data['course'], data['name'] raise error becouse of we send single data
        name = data.get('name', getattr(self.instance, 'name', None)) 
        age= data.get('age',getattr(self.instance,'age',None))
        course = data.get('course', getattr(self.instance, 'course', None))

        # if we send partial data other attributes are not present in data[''] so use variables that initialize above code 
        # use course instead of data['course'] and so on
        if course == 'BCA' and name == 'Test':
                    raise serializers.ValidationError(
                        "Test is not allowed for BCA."
            )
        return data

class StudentCreateUpdateserializerwithvalidation(serializers.ModelSerializer):
    # DRF built-in Validation/Field rule
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100,required=True,allow_blank=False,trim_whitespace=True)
    age = serializers.IntegerField(required=True,min_value=18,max_value=100)
    course = serializers.CharField(required=False,default="Degree",allow_blank=True,max_length=30)

    class Meta:
        model=Student
        fields='__all__'

    # Custom Validation
    def validate_name(self,value):
        if len(value)==0:
            raise serializers.ValidationError("Type Any Name")
        return value

    # Multiple Field Validation 
    def validate(self,data):
        name=data.get('name',getattr(self.instance,'name',None))
        age=data.get('age',getattr(self.instance,'age',None))
        course=data.get('course',getattr(self.instance,'course',None))

        if course == 'BCA' and name == 'Test':
            raise serializers.ValidationError("Test is not allowed for BCA.")
        return data
    
    # Create and Update Method
    # Normally, DRF's default create() and update() are enough. But suppose you need additional logic when creating a student. DRF custom create and update
    # Rules to remeber
    # 1. If you don't need special creation logic: Don't write create()/update()
    # 2. If you want to do something extra but still want DRF to create/update the object use:

        # for create
        # def create(self, validated_data):
        #     print("Something")
        #     return super().create(validated_data)

        # for update
        # def update(self, instance, validated_data):
        #     print("UPDATE METHOD CALLED")
        #     return super().update(instance, validated_data)

    # 3. If you want complete control over how the object is created and how object is updated: use below code
    # for create
    def create(self, validated_data):
        print("Create Method Called")
        student=Student.objects.create(
            name=validated_data['name'],
            age=validated_data['age'],
            course=validated_data['course'])
        return student

    # for update
    def update(self,instance,validated_data):
        print("Update Method Called")

        # This is useful when all fields are provided in the request so Every field MUST be present in validated_data
        # so keeping this comment
        # instance.name=validated_data['name']
        # instance.age=validated_data['age']
        # instance.course=validated_data['course']

        # This is used For partial update / PATCH
        # If a field is provided → update it
        # If a field is NOT provided → keep the existing value
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.course = validated_data.get('course', instance.course)

        instance.save()
        return instance

# What is SerializerMethodField?
# It allows you to add a custom/calculated field to the API response without adding that field to your database model.
# We can create it using: field_name = serializers.SerializerMethodField()
# SerializerMethodField does not save anything to the database, Think of it as a display/calculation field.

class StudentSerializerMethodField(serializers.ModelSerializer):

    # 1. Custom fields - New Concept(SerializerMethodField)
    student_status = serializers.SerializerMethodField()

    # 2. DRF built-in field validation - Already Learned add if needed

    class Meta:
        model = Student
        fields = 'id','name','age','course','student_status'

    # 3. Add Field validation - Already Learned add if needed
    # 4. Add Multiple-field validation - Already Learned add if needed
    # 5. Create - Already Learned add if needed
    # 6. Update - Already Learned add if needed

    # 7. Output/calculated fields - New Concept(SerializerMethodField)
    def get_student_status(self,obj):
        if obj.age>=18:
            return "Adult"
        else:
            return "Minor"

# Nested Serializer Concept
# Then why use Nested Serializer?
# Nested Serializer is mainly useful when reading related data:
class DepartmentSerializer(serializers.ModelSerializer):
    # Add Validation and Method if needed
    class Meta:
        model = Department
        fields = '__all__'

# Nested Serializer - 3 Types
# ============================================================
# 1. Nested Serializer for GET / Output
# ============================================================
class EmployeeNestedSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    # read_only=True means this nested field is used for output.
    # Example GET response:
    #
    # "department": {
    #     "id": 1,
    #     "name": "Computer"
    # }

    class Meta:
        model = Employee
        fields = '__all__'


# ============================================================
# 2. Writable Nested Serializer
# ============================================================
class EmployeeWritableNestedSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    # Writable nested data can be used for POST / PUT / PATCH.
    # Custom create() / update() logic may be required.

    class Meta:
        model = Employee
        fields = '__all__'

    # Custom create()
    # Creates a NEW Department and then creates the Employee.
    def create(self, validated_data):
        departmentdata = validated_data.pop('department')
        department = Department.objects.create(**departmentdata)
        employee = Employee.objects.create(department=department,**validated_data)
        return employee

    # Custom update()
    # Needed when we also want to update the nested Department.
    def update(self, instance, validated_data):
        departmentdata = validated_data.pop('department',None)
        instance.name = validated_data.get('name',instance.name)
        instance.salary = validated_data.get('salary',instance.salary)
        if departmentdata:
            instance.department.name = departmentdata.get('name',instance.department.name)
            instance.department.save()
        instance.save()
        return instance

# ============================================================
# 3. PrimaryKeyRelatedField
# ============================================================
class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    # Used when the Department already exists in the database.
    # POST / PUT / PATCH:
    # Send Department ID:
    # "department": 1
    # DRF converts the ID into the corresponding
    # Department object during validation.
    # The same serializer can normally be used for:
    # POST, GET, PUT and PATCH.
    # Custom create() is NOT needed.
    # Custom update() is NOT needed.
    # DRF's ModelSerializer handles them automatically.
    class Meta:
        model = Employee
        fields = '__all__'

