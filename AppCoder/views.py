"""
Please visit https://docs.djangoproject.com/en/4.1/intro/tutorial04/

In that part of the tutorial, Django documentation explains the use of generic view.
By implementing this kind of views, there is no need to elaborate in creating views, nor in the definitions
needed to display data in templates.

The details on which generic vies are avail able and how to implement them are here:
https://docs.djangoproject.com/en/4.1/ref/class-based-views/
"""
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'AppCoder/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EntriesList(ListView):
    template_name = 'AppCoder/entries_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = self.model.__name__ + "s"

        return context


# The generic view DetailView expects that the URL will pass ID of a model, in this
# case, the ID of a professor, but instead of using the field ID, pk (pk = Primary Key) should be used.
class EntryDetails(DetailView):
    template_name = 'AppCoder/entry_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = self.model.__name__

        return context


class AddEntry(CreateView):
    template_name = 'AppCoder/add_entry.html'
    fields = '__all__'
    success_url = '/'  # This is root, then index view will be displayed.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = self.model.__name__

        return context
