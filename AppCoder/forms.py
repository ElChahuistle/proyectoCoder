from django import forms


# The search form with a single field.
class StudentSearch(forms.Form):
    search = forms.CharField(label='Student', strip=True)
