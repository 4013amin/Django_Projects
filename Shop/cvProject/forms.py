from django import forms
from . import models


class loginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام کاربری خود را وارد کنید'
        }),
        label='نام کاربری'
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'رمزخود را وارد کنید ',
        })
    )


class Edit_Form_venues(forms.ModelForm):
    class Meta:
        model = models.Concert
        fields = ['title', 'description', 'price']
