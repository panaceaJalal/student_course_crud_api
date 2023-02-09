from rest_framework import serializers
from student.models import Student
from course.models import Course

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id', 'name', 'courses']
        depth=1



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'

# class StudentCourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=StudentCourse
#         fields='__all__'
    # pass