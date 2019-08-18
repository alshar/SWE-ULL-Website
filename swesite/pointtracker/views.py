from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

from users.forms import PointTrackerLoginForm


class PointTrackerLoginView(LoginView):
    template_name = 'pointtracker/pointtracker.html'
    form_class = PointTrackerLoginForm