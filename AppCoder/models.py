from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def get_courses(self):
        return Course.objects.filter(students=self)

    def get_deliverable(self):
        return Deliverable.objects.filter(studentdeliverables__student=self)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'Students'
        ordering = ['first_name', 'last_name']


class Professor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    specialty = models.CharField(max_length=30)

    def get_courses(self):
        return Course.objects.filter(professor=self)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'Professors'
        ordering = ['first_name', 'last_name']


class Course(models.Model):
    name = models.CharField(max_length=40)
    attendees = models.IntegerField()
    students = models.ManyToManyField(Student)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True, default=None)

    def get_students(self):
        return self.students.all()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Courses'
        ordering = ['name']


class Deliverable(models.Model):
    name = models.CharField(max_length=30)
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.course})'

    class Meta:
        verbose_name_plural = 'Deliverables'
        ordering = ['name']


class StudentDeliverables(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    deliverable = models.ForeignKey(Deliverable, on_delete=models.CASCADE)
    delivered = models.BooleanField()
