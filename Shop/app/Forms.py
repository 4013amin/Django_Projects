from django import forms


class SearchForm(forms.Form):
    textFiled = forms.CharField(max_length=200, required=False)
