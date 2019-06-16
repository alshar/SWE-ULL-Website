from django.template.response import TemplateResponse


def volunteerpoints(request):
    return TemplateResponse(request, 'volunteerpoints/volunteerpoints.html')