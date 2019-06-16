from django.template.response import TemplateResponse


def pointtracker(request):
    return TemplateResponse(request, 'pointtracker/pointtracker.html')
