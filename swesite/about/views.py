from django.views.generic import TemplateView
from about.swe_officers_context import swe_officers_primary, swe_officers_secondary, swe_officers_tertiary


class about(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super(about, self).get_context_data(**kwargs)
        context['swe_officers_primary'] = swe_officers_primary(request=about)
        context['swe_officers_secondary'] = swe_officers_secondary(request=about)
        context['swe_officers_tertiary'] = swe_officers_tertiary(request=about)
        return context
