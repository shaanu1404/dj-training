from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()


class UserCreateForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirm password')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        widgets = {
            "password": forms.PasswordInput
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        password2 = cleaned_data['password2']

        if password2 != password:
            raise forms.ValidationError("Passwords don't match")

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)