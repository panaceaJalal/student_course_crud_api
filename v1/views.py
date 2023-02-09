from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from student.models import Student
from course.models import Course
from .serializers import  StudentSerializer, CourseSerializer

# Create your views here.


# class StudentViewSet(viewsets.ModelViewsets):
#     serializer_class=StudentSerializer

#     def get_queryset(self):
#         student=Student.objects.all()
#         return student

# class CourseViewSet(viewsets.ModelViewsets):
#     serializer_class=CourseSerializer

#     def get_queryset(self):
#         student=Course.objects.all()
#         return student
             
# ---------------------------------------
# -------------1st approuch---------------
class studentCoursesView(generics.ListAPIView):
    serializer_class=CourseSerializer
    def get_queryset(self):
        queryset=Student.objects.get(id=self.id)
        print(queryset)
        return queryset
# ---------------------
class StudentList(generics.ListCreateAPIView):
    serializer_class=StudentSerializer
    def get_queryset(self):
        queryset=Student.objects.all()
        return queryset

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()

class CourseList(generics.ListCreateAPIView):
    serializer_class=CourseSerializer
    queryset=Course.objects.all()

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=CourseSerializer
    queryset=Course.objects.all()

# class StudentCourseList(generics.ListCreateAPIView):
#     serializer_class=StudentCourseSerializer
#     queryset=StudentCourse.objects.all()

# class StudentCourseDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class=StudentCourseSerializer
#     queryset=StudentCourse.objects.all()

# class StudentCoursesList(generics.ListCreateAPIView):
#     serializer_class=StudentCourseSerializer
#     def get_queryset(self):
#         std=Student.objects.get()
#         return super().get_queryset()

# ------------2nd approch---------------
class studentAPI(APIView):
    def get(self, request):
        students=Student.objects.all()
        serializer=StudentSerializer(students, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)# else 
        # -------------------------------------------------------
# class studentCourses(APIView):
#     def get_student(self,pk):
#         try:
#             return Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             return Response(StudentSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def get(self,request,pk):
#         std=self.get_student(pk)
#         courses=StudentCourse.objects.filter(studentId=std)
#         serializer=StudentCourseSerializer(courses)

        # std_courses=StudentCourse.objects.filter(studentId_id=std.id)#now we have all courses of the student
        # serializer=StudentCourseSerializer(std_courses)    
        # std_courses=Course.objects.all()
        return Response(serializer.data)
        # -------------------------------------------------------
class UpdateDelStudent(APIView):
    def get_object(self,pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(StudentSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request, pk):
        std=self.get_object(pk)
        serialize=StudentSerializer(std) 
        return Response(serialize.data)
    def put(self,request,pk):
        std=self.get_object(pk)
        serializer=StudentSerializer(std, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)# else 
    def delete(self,request, pk):
        std=Student.objects.get(pk=pk)
        std.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
class CourseAPI(APIView):
    def get(self,request):
        courses=Course.objects.all()
        serializer=CourseSerializer(courses, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)# else 
class UpdateDelCourse(APIView):
    def get_obj(self,pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(CourseSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,pk):
        course=Course.objects.get(pk=pk)
        serializer=CourseSerializer(course)
        return Response(serializer.data)
    def put(self,request,pk):
        course=self.get_obj(pk)
        serializer=CourseSerializer(course, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)# else 
    
    def delete(self, request, pk):
        course=Course.objects.get(pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
