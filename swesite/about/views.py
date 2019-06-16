from django.template.response import TemplateResponse


def about(request):
    return TemplateResponse(request, 'about/about.html')