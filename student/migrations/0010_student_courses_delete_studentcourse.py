# Generated by Django 4.1.1 on 2023-01-27 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_rename_coursename_course_name'),
        ('student', '0009_alter_student_address_alter_student_fathername_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='course.course'),
        ),
        migrations.DeleteModel(
            name='StudentCourse',
        ),
    ]
