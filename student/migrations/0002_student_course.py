# Generated by Django 4.1.5 on 2023-01-24 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_remove_course_students'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(to='course.course'),
        ),
    ]