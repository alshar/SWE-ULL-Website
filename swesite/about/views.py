from django.views.generic import TemplateView
from swesite.contexts.swe_social_context import swe_social
from swesite.contexts.swe_officers_context import swe_officers_context


class about(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super(about, self).get_context_data(**kwargs)
        context['swe_officers_context'] = swe_officers_context(request=about)
        context['swe_social'] = swe_social(request=about)
        return context
