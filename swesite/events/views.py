from django.views.generic import TemplateView
from swesite.contexts.swe_events_context import SPRING_20_CONTEXT, FALL_19_CONTEXT
from swesite.contexts.swe_social_context import swe_social


# the html file and context object needs to be changed every semester
class events(TemplateView):
    template_name = 'events/spring_20_gallery.html'

    def get_context_data(self, **kwargs):
        context = super(events, self).get_context_data(**kwargs)
        context['event_data'] = SPRING_20_CONTEXT
        context['swe_social'] = swe_social(request=events)
        return context


class fall19(TemplateView):
    template_name = 'events/fall_19_gallery.html'

    def get_context_data(self, **kwargs):
        context = super(fall19, self).get_context_data(**kwargs)
        context['event_data'] = FALL_19_CONTEXT
        context['swe_social'] = swe_social(request=events)
        return context


class spring19(TemplateView):
    template_name = 'events/spring_19_gallery.html'

    def get_context_data(self, **kwargs):
        context = super(spring19, self).get_context_data(**kwargs)
        context['swe_social'] = swe_social(request=events)
        return context


class fall18(TemplateView):
    template_name = 'events/fall18gallery.html'

    def get_context_data(self, **kwargs):
        context = super(fall18, self).get_context_data(**kwargs)
        context['swe_social'] = swe_social(request=events)
        return context


class spring18(TemplateView):
    template_name = 'events/spring18gallery.html'

    def get_context_data(self, **kwargs):
        context = super(spring18, self).get_context_data(**kwargs)
        context['swe_social'] = swe_social(request=events)
        return context
