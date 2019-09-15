from django.views.generic import TemplateView

from swesite.contexts.swe_social_context import swe_social


class PointTrackerLogin(TemplateView):
    template_name = 'pointtracker/pointtracker.html'

    def get_context_data(self, **kwargs):
        context = super(PointTrackerLogin, self).get_context_data(**kwargs)
        context['swe_social'] = swe_social(request=PointTrackerLogin)
        return context
