from django import forms
from . import models

class Login_Forms(forms.Form):
    class Meta:
        model = models.Profile
        field = ['name', 'phone']
        


class OTPForm(forms.Form):
    code = forms.CharField(
        label="کد تایید",
        max_length=4,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autocomplete': 'one-time-code',
            'placeholder': 'کد ارسال‌شده را وارد کنید'
        })
    )
