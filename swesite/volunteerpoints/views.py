from django.views.generic import TemplateView
from swesite.contexts.swe_social_context import swe_social
from swesite.contexts.swe_volunteer_context import swe_volunteer
from swesite.contexts.swe_officers_context import swe_officers_context


class volunteerpoints(TemplateView):
    template_name = 'volunteerpoints/volunteerpoints.html'

    def get_context_data(self, **kwargs):
        context = super(volunteerpoints, self).get_context_data(**kwargs)
        context['swe_volunteer'] = swe_volunteer(request=volunteerpoints)
        context['swe_social'] = swe_social(request=volunteerpoints)
        context['swe_officers_context'] = swe_officers_context(request=volunteerpoints)
        return context