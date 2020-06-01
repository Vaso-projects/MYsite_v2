from django import forms


class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailInput()
    password = forms.PasswordInput
