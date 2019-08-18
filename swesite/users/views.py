from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import SWEUserCreationForm


class SignUpView(CreateView):
    form_class = SWEUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
