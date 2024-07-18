from django import forms
from .models import Data


class Search_form(forms.Form):
    text_filed = forms.CharField(max_length=30, required=False)


class FormEdit(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['username', 'title', 'Date', 'image']
