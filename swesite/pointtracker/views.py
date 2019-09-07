from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

# from pointtracker.forms import SWEUserLogin


class PointTrackerLogin(TemplateView):
    template_name = 'pointtracker/pointtracker.html'
    # authentication_form = SWEUserLogin
