from django.views.generic import TemplateView
from swesite.contexts.swe_social_context import swe_social


class events(TemplateView):
    template_name = 'events/events.html'


class spring19(TemplateView):
    template_name = 'events/spring_19_gallery.html'

class fall18(TemplateView):
    template_name = 'events/fall18gallery.html'


class spring18(TemplateView):
    template_name = 'events/spring18gallery.html'