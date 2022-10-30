from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.HyperlinkedModeSerializer):
    class Meta:
        model = Student 
        field = '__all__'
        # fields = ("stu_id" , "stu_name")

