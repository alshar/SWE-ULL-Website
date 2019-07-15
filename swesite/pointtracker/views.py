from django.contrib.auth.views import LoginView
from pointtracker.forms import SWEUserLogin


class PointTrackerLogin(LoginView):
    template_name = 'pointtracker/pointtracker.html'
    form = SWEUserLogin