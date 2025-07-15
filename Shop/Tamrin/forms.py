from django import forms
from . import models


class Profile_form(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['user', 'phone']


class Tasks_form(forms.ModelForm):
    class Meta:
        model = models.Tasks
        fields = ['title', 'description']
