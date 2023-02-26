"""
Please visit https://docs.djangoproject.com/en/4.1/intro/tutorial04/

In that part of the tutorial, Django documentation explains the use of generic views.
By implementing this kind of views, there is no need to create a view for each model,
nor a different template for each view.

The details on which generic vies are available and how to implement them are here:
https://docs.djangoproject.com/en/4.1/ref/class-based-views/

One of the advantages of using a generic view is that the class by default handles
the request method, querying the data based on the indicated model and the resulting template.
"""
from django.views.generic import CreateView, DetailView, ListView, FormView
from django.views.generic.base import TemplateView
from django.db.models import Q  # The class Q is used for complex filtering, say many ANDs or ORs.

from AppCoder.forms import StudentSearch
from AppCoder.models import Student


# In this particular case, the use of the TemplateView is just to display a template.
class IndexView(TemplateView):
    template_name = 'AppCoder/index.html'


# WIth this view, the full list of elements for a given model will be displayed. The objects
# to be used by the template can change by overriding the method get_queryset (check view StudentSearchResults).
class EntriesList(ListView):
    template_name = 'AppCoder/entries_list.html'

    # This override is to "pluralize" the name of the model to be used as a heading in the template.
    def get_context_data(self, **kwargs):
        # Because it is an override, first get the context created by default,
        # then update it to have the pluralized name of the model, then return
        # the new context to be used by the template.
        context = super().get_context_data(**kwargs)
        context['heading'] = self.model.__name__ + "s"

        return context


# The generic view DetailView expects that the URL will pass ID of a model, in this
# case, the ID of a professor, but instead of using the field ID, pk (pk = Primary Key) should be used.
class EntryDetails(DetailView):
    template_name = 'AppCoder/entry_details.html'

    # This override is to get the name of the model to be used as a heading in the template.
    def get_context_data(self, **kwargs):
        # Because it is an override, first get the context created by default,
        # then update it to have the name of the model, then return the new
        # context to be used by the template.
        context = super().get_context_data(**kwargs)
        context['heading'] = self.model.__name__

        return context


# By implementing the CreateView generic view there is no need to create a
# form, this view takes a model and from it creates a form to add new objects.
class AddEntry(CreateView):
    template_name = 'AppCoder/add_entry.html'
    fields = '__all__'  # This value can be change to a list with the names of the fields to be used.
    success_url = '/'  # This is root, then index view will be displayed.

    # This override is to get the name of the model to be used as a heading in the template.
    def get_context_data(self, **kwargs):
        # Because it is an override, first get the context created by default,
        # then update it to have the name of the model, then return the new
        # context to be used by the template.
        context = super().get_context_data(**kwargs)
        context['heading'] = self.model.__name__

        return context


class StudentSearchView(FormView):
    form_class = StudentSearch
    template_name = 'AppCoder/search_student.html'


# Just as EntriesList, but it receives a parameter from the search form to query (in this
# case) the Student model with the value in "search" parameter got from the GET request.
class StudentSearchResults(ListView):
    model = Student  # This view will use only the Student model.
    template_name = 'AppCoder/student_search_results.html'

    # This override changes the data that will be returned by the view.
    def get_queryset(self):
        # In case the method is not GET, or no search parameters are receive, return nothing
        # by using a value that does not exist in the db.
        queryset = Student.objects.get(pk=-1)

        # This block is redundant, because this view will be invoked only when from
        # the search form and only for Student model, but if more models are needed,
        # there is needed to update it to decided how to query the data.
        #
        # Also, it is possible to reuse EntriesList to handle the search results instead
        # of this view, and this block could be used as a reference to update EntriesList.
        if self.request.method == 'GET':
            if self.request.GET.get('search'):

                # The parameter passe by will be searched in first and last name, that is
                # why a Q object is being used for each case.
                queryset = Student.objects.filter(
                    Q(first_name=self.request.GET.get('search'))
                    | Q(last_name=self.request.GET.get('search'))
                )

        return queryset
