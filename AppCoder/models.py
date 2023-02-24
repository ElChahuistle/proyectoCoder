from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=40)
    attendees = models.IntegerField()

    def __str__(self) -> str:
        return self.name + ' (' + str(self.attendees) + ')'

    class Meta:
        ordering = ['name']


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']


class Professor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    specialty = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']


class Deliverable(models.Model):
    name = models.CharField(max_length=30)
    due_date = models.DateField()
    delivered = models.BooleanField()

    def __str__(self):
        return f'{self.name}'
