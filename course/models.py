from django.db import models
# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=50,verbose_name='Course Name')
    def __str__(self):
        return self.name