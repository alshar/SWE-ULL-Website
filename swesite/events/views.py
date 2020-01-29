from django.views.generic import TemplateView
from swesite.contexts.swe_events_context import fall_19, fall_20
from swesite.contexts.swe_social_context import swe_social


class events(TemplateView):
    template_name = 'events/events.html'

    def get_context_data(self, **kwargs):
        context = super(events, self).get_context_data(**kwargs)
        context['fall_20'] = fall_20(request=events)
        context['swe_social'] = swe_social(request=events)
        return context


class fall19(TemplateView):
    template_name = 'events/fall19gallery.html'

    def get_context_data(self, **kwargs):
        context = super(fall19, self).get_context_data(**kwargs)
        context['swe_social'] = swe_social(request=events)
        context['fall_19'] = fall_19(request=events)
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
