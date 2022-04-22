from allauth.account.forms import SignupForm
from django import forms as as_forms
from django.contrib.auth import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms.models import ModelForm
from .models import User


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User


class MyCustomSignupForm(SignupForm):
    first_name = as_forms.CharField(max_length=30, label='Nome')

    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = as_forms.TextInput(attrs={'placeholder': 'Nome'})

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.save()
        return user
