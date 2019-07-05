from django.views.generic import TemplateView
from swesite.contexts.swe_social_context import swe_social
from swesite.contexts.swe_officers_context import swe_officers_primary, swe_officers_secondary, swe_officers_tertiary


class about(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super(about, self).get_context_data(**kwargs)
        context['swe_officers_primary'] = swe_officers_primary(request=about)
        context['swe_officers_secondary'] = swe_officers_secondary(request=about)
        context['swe_officers_tertiary'] = swe_officers_tertiary(request=about)
        context['swe_social'] = swe_social(request=about)
        return context
