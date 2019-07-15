from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder, Fieldset
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SWEUserCreation(UserCreationForm):
    pass


class SWEUserLogin(AuthenticationForm):
    pass