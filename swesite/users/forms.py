from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import SWEUser


class SWEUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = SWEUser
        fields = ('username', 'email')


class SWEUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = SWEUser
        fields = ('username', 'email')
