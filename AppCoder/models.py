from django.db import models


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


class Course(models.Model):
    """
    Relationships:
        A Course has one and oly one professor, but a professor might have many courses.
        A Course could have many students. The use of a ManyToManyField implies that a Student could have many courses,
          and by doing this there is no need to 1) Reference a Course in Student, adn 2) Create a third model to
          related Student and Course.
    """
    name = models.CharField(max_length=40)
    # attendees = models.IntegerField()
    students = models.ManyToManyField(Student)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True, default=None)

    def get_students(self):
        return self.students.all()

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']


class Deliverable(models.Model):
    """
    Relationship:
        A Deliverable will be related to one and only one Course, but Course have many Deliverables.
    """
    name = models.CharField(max_length=30)
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.course})'

    class Meta:
        ordering = ['name']


class StudentDeliverables(models.Model):
    """
    A Student could have one or many deliverables, and vice-vers.
    """
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    deliverable = models.ForeignKey(Deliverable, on_delete=models.CASCADE)
    delivered = models.BooleanField()
