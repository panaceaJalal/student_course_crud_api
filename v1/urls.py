from django.contrib import admin
from django.urls import path
from .views import StudentList,StudentDetail,CourseList,UpdateDelStudent ,CourseDetail, studentAPI,CourseAPI,UpdateDelCourse
from v1 import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
# router.register('student', StudentViewSet, basename='student')
# router.register('course', CourseViewSet, basename='course')
# https://www.youtube.com/watch?v=NCBxyw6rDds  
urlpatterns = [
path('student/', StudentList.as_view()),
path('student/<int:pk>/', StudentDetail.as_view()),
path('course/', CourseList.as_view()),
path('course/<int:pk>/', CourseDetail.as_view()),
# path('studentCourse/', StudentCourseList.as_view()),
# path('studentCourse/<int:pk>/', StudentCourseDetail.as_view()),

path('students/', studentAPI.as_view()),
path('students/<int:pk>/', UpdateDelStudent.as_view()),
path('courses/', CourseAPI.as_view()),
path('courses/<int:pk>/', UpdateDelCourse.as_view()),
# path('studentCourses/<int:pk>/', studentCourses.as_view())


]
