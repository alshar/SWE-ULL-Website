from django.views.generic import TemplateView
from swesite.contexts.swe_volunteer_context import swe_volunteer


class volunteerpoints(TemplateView):
    template_name = 'volunteerpoints/volunteerpoints.html'

    def get_context_data(self, **kwargs):
        context = super(volunteerpoints, self).get_context_data(**kwargs)
        context['swe_volunteer'] = swe_volunteer(request=volunteerpoints)
        return context