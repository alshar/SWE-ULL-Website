from django.views.generic import TemplateView
from swesite.contexts.swe_events_context import fall_19


class events(TemplateView):
    template_name = 'events/events.html'

    def get_context_data(self, **kwargs):
        context = super(events, self).get_context_data(**kwargs)
        context['fall_19'] = fall_19(request=events)
        return context

class spring19(TemplateView):
    template_name = 'events/spring_19_gallery.html'

class fall18(TemplateView):
    template_name = 'events/fall18gallery.html'


class spring18(TemplateView):
    template_name = 'events/spring18gallery.html'