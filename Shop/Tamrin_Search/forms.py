from django import forms


class Search_form(forms.Form):
    text_filed = forms.CharField(max_length=30, required=False)

