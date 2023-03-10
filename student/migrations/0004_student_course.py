# Generated by Django 4.1.5 on 2023-01-24 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_remove_course_students'),
        ('student', '0003_remove_student_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
