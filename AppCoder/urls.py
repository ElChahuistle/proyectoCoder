from django.urls import path

from AppCoder import views
from AppCoder.models import Course, Student, Professor

# Adding variable "app_name" there is no need to write the whole URL in a:href tags.
# The notation app:name will suffice. In the case of AppCoder, for example a link to
# index should be: <a href:"{% url AppCoder:index %}">Index</a>
#
# NOTE: Going forward, when using {% url ... %} in any template should follow the
# notation AppCoder:[ViewName].
app_name = 'AppCoder'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('professors/', views.EntriesList.as_view(model=Professor), name='professors'),
    path('professor/<int:pk>/', views.EntryDetails.as_view(model=Professor), name='professor'),
    path('professor/add/', views.AddEntry.as_view(model=Professor), name='add_professor'),
    path('courses/', views.EntriesList.as_view(model=Course), name='courses'),
    path('course/<int:pk>/', views.EntryDetails.as_view(model=Course), name='course'),
    path('course/add/', views.AddEntry.as_view(model=Course), name='add_course'),
    path('students/', views.EntriesList.as_view(model=Student), name='students'),
    path('student/<int:pk>/', views.EntryDetails.as_view(model=Student), name='student'),
    path('student/add/', views.AddEntry.as_view(model=Student), name='add_student'),
]
