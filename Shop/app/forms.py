from django import forms
from . import models

class Login_Forms(forms.Form):
    class Meta:
        model = models.Profile
        field = ['name', 'phone']
        


class OTP(forms.Form):
    phone = forms.CharField(
        label='شماره تماس',
        max_length=11,
    )

    code = forms.CharField(
        label="کد",
        max_length=4,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autocomplete': 'one-time-code',
            'placeholder': 'کد ۶ رقمی ارسال شده را وارد کنید'
        })
    )
