from rest_framework import serializers
from api.models import Employee
from SearchAPIView.models import Course
from AuthApp.models import Note

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields='__all__'
        read_only_fields = ["owner"]