# Generated by Django 4.1.5 on 2023-01-24 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_rename_course_id_student_course_course_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_course',
            old_name='Course_id',
            new_name='courseId',
        ),
        migrations.RenameField(
            model_name='student_course',
            old_name='Student_id',
            new_name='studentId',
        ),
    ]
