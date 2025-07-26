from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
class BookSearchForm(forms.Form):
    title = forms.CharField(required=False, max_length=100)