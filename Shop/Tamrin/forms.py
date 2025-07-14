from django import forms
from . import models


class Tasks_form(forms.ModelForm):
    class Meta:
        model = models.Tasks
        fields = ['title', 'description']
