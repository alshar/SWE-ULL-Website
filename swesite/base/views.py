from django.views.generic import TemplateView
from swesite.contexts.swe_social_context import swe_social
from swesite.contexts.swe_volunteer_context import swe_volunteer


class baseindex(TemplateView):
    template_name = 'base/base.html'

    def get_context_data(self, **kwargs):
        context = super(baseindex, self).get_context_data(**kwargs)
        context['swe_social'] = swe_social(request=baseindex)
        context['swe_volunteer'] = swe_volunteer(request=baseindex)
        return context

