# Generated by Django 4.1.5 on 2023-01-26 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_course_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='courseName',
        ),
    ]
