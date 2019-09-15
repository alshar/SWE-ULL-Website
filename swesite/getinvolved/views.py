from django.views.generic import TemplateView
from swesite.contexts.swe_social_context import swe_social


class getinvolved(TemplateView):
    template_name = 'getinvolved/getinvolved.html'

    def get_context_data(self, **kwargs):
        context = super(getinvolved, self).get_context_data(**kwargs)
        context['swe_social'] = swe_social(request=getinvolved)
        return context
