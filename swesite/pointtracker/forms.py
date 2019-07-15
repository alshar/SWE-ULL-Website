from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder, Fieldset
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SWEUserCreation(UserCreationForm):
    pass


class SWEUserLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(SWEUserLogin, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Login',
                'username',
                'password'
            ),
            ButtonHolder(
                Submit('submit', 'Submit')
            )
        )