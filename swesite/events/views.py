from django.template.response import TemplateResponse


def events(request):
    return TemplateResponse(request, 'events/events.html')


def fall18(request):
    return TemplateResponse(request, 'events/fall18gallery.html')


def spring18(request):
    return TemplateResponse(request, 'events/spring18gallery.html')