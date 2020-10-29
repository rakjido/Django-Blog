from django.contrib.auth.models import User
from django import forms
from django.forms import fields


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email")

    def clean_password2(self):
        acct = self.cleaned_data
        if acct["password"] != acct["password2"]:
            raise forms.ValidationError("Passwords don't match.")
