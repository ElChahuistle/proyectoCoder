# Generated by Django 4.1.7 on 2023-02-26 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('AppCoder', '0001_initial'), ('AppCoder', '0002_professor_students_rename_curso_course_and_more'), ('AppCoder', '0003_rename_students_student'), ('AppCoder', '0004_alter_course_options_alter_deliverable_options_and_more')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('specialty', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
                'verbose_name_plural': 'Professors',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('attendees', models.IntegerField()),
                ('professor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AppCoder.professor')),
                ('students', models.ManyToManyField(to='AppCoder.student')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Deliverable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('due_date', models.DateField()),
                ('course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AppCoder.course')),
                ('professor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AppCoder.professor')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Deliverables',
            },
        ),
        migrations.CreateModel(
            name='StudentDeliverables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivered', models.BooleanField()),
                ('deliverable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCoder.deliverable')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCoder.student')),
            ],
        ),
    ]
