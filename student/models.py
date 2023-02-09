from django.db import models
from course.models import Course
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50, verbose_name='Student Name')
    fatherName=models.CharField(max_length=50, verbose_name='Father Name', null=True)
    address=models.CharField(max_length=255, verbose_name='Adress', null=True)
    courses=models.ManyToManyField(Course)
    def __str__(self):
        return self.name

# class StudentCourse(models.Model):
#     studentId=models.ForeignKey(Student, on_delete=models.CASCADE)
#     courseId=models.ForeignKey(Course, on_delete=models.CASCADE)
#     def __str__(self):
#         return f'{self.studentId.name}: {self.courseId.name}'