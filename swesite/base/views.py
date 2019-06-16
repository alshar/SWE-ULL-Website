from django.template.response import TemplateResponse


def baseindex(request):
    return TemplateResponse(request, 'base/base.html')