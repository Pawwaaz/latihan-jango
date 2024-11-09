from django import forms
from django.core import validators

def check_for_uppcase(value):
    if not value[0].isupper():
        raise forms.ValidationError("Huruf pertama harus kapital") 

class FormName (forms.Form):
    name = forms.CharField(max_length=100, validators=[check_for_uppcase])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput, validators=[validators.MinLengthValidator(8)])

    def clean(self):
        return super().clean()
        email = all_clean_data['email']


