from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder, Fieldset, Div, Row, Column, HTML
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SWEUserCreation(UserCreationForm):
    pass


class SWEUserLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(SWEUserLogin, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_class = 'card justify-content-center text-center'
        self.helper.layout = Layout(
            Fieldset(
                'Log In',
                Div(
                    Column(
                        Row('username', css_class='justify-content-center'),
                        Row('password', css_class='justify-content-center'),
                        Row(Submit('submit', 'Log In', css_class='justify-content-center'),
                            css_class='justify-content-center'),
                        css_class='container'),

                )
            )
        )
