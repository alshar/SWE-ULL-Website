from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder, Fieldset, Div, Row, Column, HTML, Field
from django import forms
from django.urls import reverse


class PointTrackerLoginForm(forms.Form):
    ulid = forms.CharField(
        label="ULID",
        required=True,
        max_length=9
    )

    first_name = forms.CharField(
        label="First Name",
        required=True,
        max_length=80
    )

    last_name = forms.CharField(
        label="Last Name",
        required=True,
        max_length=80
    )

    def __init__(self, *args, **kwargs):
        super(PointTrackerLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_class = 'justify-content-center text-center'
        self.helper.field_class = ''
        self.helper.form_action = reverse('pointtracker')

        self.helper.layout = Layout(
            Field('first_name'),
            Field('last_name'),
            Field('ulid'),

            Submit('submit', 'Submit', css_class='btn btn-primary mt-4')
        )
