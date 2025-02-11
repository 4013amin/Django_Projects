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
        fields = ['title', 'description', 'price', 'image']


# Register Form
class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(widget=forms.EmailInput)

    class Meta:
        model = models.Profile
        fields = ['credit', 'image', 'gender']


# contact us
class Form_Contact_Us(forms.ModelForm):
    class Meta:
        model = models.ContactUs
        fields = '__all__'
