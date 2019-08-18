from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from users.forms import PointTrackerLoginForm, SWEUserCreationForm


class PointTrackerLoginView(LoginView):
    template_name = 'pointtracker/pointtracker.html'
    form_class = PointTrackerLoginForm


class PointTrackerSignUpView(CreateView):
    form_class = SWEUserCreationForm
    success_url = reverse_lazy('pointtracker')
    template_name = 'pointtracker/signup.html'
