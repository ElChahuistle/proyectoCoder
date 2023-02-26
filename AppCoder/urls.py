from django.urls import path

from AppCoder.models import Course, Professor, Student
from AppCoder.views import AddEntry, EntriesList, EntryDetails, IndexView, StudentSearchResults, StudentSearchView

"""
Adding variable "app_name" there is no need to write the whole URL in a:href tags.
The notation app:name will suffice. In the case of AppCoder, for example a link to
index should be: <a href:"{% url AppCoder:index %}">Index</a>

NOTE: Going forward, when using {% url ... %} in any template should follow the
notation AppCoder:[name].

To take advantage of the generic view, and with the exception of the search, the model 
is being passed as an argument to the view, so the same view can be reused. Each template 
will handle how to display the corresponding data.
"""
app_name = 'AppCoder'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('professors/', EntriesList.as_view(model=Professor), name='professors'),
    path('professor/<int:pk>/', EntryDetails.as_view(model=Professor), name='professor'),
    path('professor/add/', AddEntry.as_view(model=Professor), name='add_professor'),
    path('courses/', EntriesList.as_view(model=Course), name='courses'),
    path('course/<int:pk>/', EntryDetails.as_view(model=Course), name='course'),
    path('course/add/', AddEntry.as_view(model=Course), name='add_course'),
    path('students/', EntriesList.as_view(model=Student), name='students'),
    path('student/<int:pk>/', EntryDetails.as_view(model=Student), name='student'),
    path('student/add/', AddEntry.as_view(model=Student), name='add_student'),
    path('students/search/', StudentSearchView.as_view(), name='search_student'),
    path('students/search/resultsa', StudentSearchResults.as_view(), name='search_results_student'),
]
