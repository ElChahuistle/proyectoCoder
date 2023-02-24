"""
Please visit https://docs.djangoproject.com/en/4.1/intro/tutorial04/

In that part of the tutorial, Django documentation explains the use of generic view.
By implementing this kind of views, there is no need to elaborate in creating views, nor in the definitions
needed to display data in templates.

The details on which generic vies are avail able and how to implement them are here:
https://docs.djangoproject.com/en/4.1/ref/class-based-views/
"""
from django.views import generic
from django.views.generic.base import TemplateView

from .models import Professor, Course, Student


class IndexView(TemplateView):
    template_name = 'AppCoder/index.html'


class ProfessorsListView(generic.ListView):
    template_name = 'AppCoder/content_list.html'
    extra_context = {'model': 'Professors'}

    # This is an override of the method get:_queryset to indicate this view which
    # objects should be displayed, in this particular case, every professor.
    def get_queryset(self):
        return Professor.objects.all()


# The generic view DetailView expects that the URL will pass ID of a model, in this
# case, the ID of a professor, but instead of using the field ID, pk (pk = Primary Key) should be used.
class ProfessorView(generic.DetailView):
    model = Professor
    template_name = 'AppCoder/details.html'
    extra_context = {'model': 'Professor'}


# There are twi things to notice here:
# 1. This view implements the mode Professor, by doing this the generated view will be linked directly to the model,
#   so when the data is submit it will be saved directly to the database.
# 2. The fields to be displayed can be selected in fields variable, in this all of them are been shown, otherwise
#   create list of the ones needed.
class ProfessorCreateView(generic.CreateView):
    model = Professor
    fields = "__all__"
    extra_context = {'model': 'Professor'}
    template_name = 'AppCoder/add_new_object.html'
    success_url = '/'  # This is root, then index view will be displayed.

# From here on, all the view are going to follow same structure than the previous ones.


class CoursesListView(generic.ListView):
    template_name = 'AppCoder/content_list.html'
    extra_context = {'model': 'Courses'}

    # This is an override of the method get:_queryset to indicate this view which
    # objects should be displayed, in this particular case, every professor.
    def get_queryset(self):
        return Course.objects.all()


class CourseView(generic.DetailView):
    model = Professor
    template_name = 'AppCoder/details.html'
    extra_context = {'model': 'Course'}


class CourseCreateView(generic.CreateView):
    model = Course
    fields = "__all__"
    template_name = 'AppCoder/add_new_object.html'
    extra_context = {'model': 'Course'}
    success_url = '/'  # This is root, then index view will be displayed.


class StudentsListView(generic.ListView):
    template_name = 'AppCoder/content_list.html'
    extra_context = {'model': 'Students'}

    # This is an override of the method get:_queryset to indicate this view which
    # objects should be displayed, in this particular case, every professor.
    def get_queryset(self):
        return Student.objects.all()


class StudentView(generic.DetailView):
    model = Student
    template_name = 'AppCoder/details.html'
    extra_context = {'model': 'Student'}


class StudentCreateView(generic.CreateView):
    model = Student
    fields = "__all__"
    template_name = 'AppCoder/add_new_object.html'
    extra_context = {'model': 'Student'}
    success_url = '/'  # This is root, then index view will be displayed.
