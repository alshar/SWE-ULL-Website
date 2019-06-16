from django.template.response import TemplateResponse


def baseindex(request):
    return TemplateResponse(request, 'base/baseindex.html')