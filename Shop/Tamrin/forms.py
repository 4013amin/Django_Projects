from django import forms
from .models import ProfileUser


class RegisterProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    image = forms.ImageField(required=False)

    class Meta:
        model = ProfileUser
        fields = ['username', 'password', 'phone', 'image']
