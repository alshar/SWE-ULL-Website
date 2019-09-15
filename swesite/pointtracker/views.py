from django.views.generic import FormView

from pointtracker.forms import PointTrackerLoginForm
from swesite.contexts.swe_social_context import swe_social


class PointTrackerLoginView(FormView):
    template_name = 'pointtracker/pointtracker.html'
    form_class = PointTrackerLoginForm

    def get_context_data(self, **kwargs):
        context = super(PointTrackerLoginView, self).get_context_data(**kwargs)
        context['swe_social'] = swe_social(request=PointTrackerLoginView)
        return context


