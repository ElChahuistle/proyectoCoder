
from django.urls import path

from AppCoder import views


# Adding variable "app_name" there is no need to write the whole URL in a:href tags.
# The notation app:name will suffice. In the case of AppCoder, for example a link to
# index should be: <a href:"{% url AppCoder:index %}">Index</a>
#
# NOTE: Going forward, when using {% url ... %} in any template should follow the
# notation AppCoder:[ViewName].
app_name = 'AppCoder'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('professors/', views.ProfessorsListView.as_view(), name='professors'),
    path('professor/<int:pk>/', views.ProfessorView.as_view(), name='professor'),
    path('professor/add/', views.ProfessorCreateView.as_view(), name='add_professor'),
    path('courses/', views.CoursesListView.as_view(), name='courses'),
    path('course/<int:pk>/', views.CourseView.as_view(), name='course'),
    path('course/add/', views.CourseCreateView.as_view(), name='add_course'),
    path('students/', views.StudentsListView.as_view(), name='students'),
    path('student/<int:pk>/', views.StudentView.as_view(), name='student'),
    path('student/add/', views.StudentCreateView.as_view(), name='add_student'),
]
