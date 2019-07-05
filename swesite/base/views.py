from django.views.generic import TemplateView
from swesite.contexts.swe_social_context import swe_social


class baseindex(TemplateView):
    template_name = 'base/base.html'

    def get_context_data(self, **kwargs):
        context = super(baseindex, self).get_context_data(**kwargs)
        context['swe_social'] = swe_social(request=baseindex)
        return context

