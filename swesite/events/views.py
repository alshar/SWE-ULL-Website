from django.views.generic import TemplateView
from swesite.contexts.swe_social_context import swe_social


class events(TemplateView):
    template_name = 'events/events.html'

    def get_context_data(self, **kwargs):
        context = super(events, self).get_context_data(**kwargs)
        context['swe_social'] = swe_social(request=events)
        return context



class fall18(TemplateView):
    template_name = 'events/fall18gallery.html'


class spring18(TemplateView):
    template_name = 'events/spring18gallery.html'