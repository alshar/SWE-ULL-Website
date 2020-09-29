from django.views.generic import TemplateView
from swesite.contexts.swe_events_context import past_events
from swesite.contexts.swe_social_context import swe_social


# the html file and context object needs to be changed every semester
class Events(TemplateView):
    template_name = 'events/current_events.html'

    def get_context_data(self, **kwargs):
        context = super(Events, self).get_context_data(**kwargs)
        context['swe_social'] = swe_social(request=Events)
        return context


class PastEvents(TemplateView):
    template_name = 'events/past_events.html'

    def get_context_data(self, **kwargs):
        context = super(PastEvents, self).get_context_data(**kwargs)
        context['event_data'] = past_events
        context['swe_social'] = swe_social(request=Events)
        return context


