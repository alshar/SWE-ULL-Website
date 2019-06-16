from django.template.response import TemplateResponse

def getinvolved(request):
    return TemplateResponse(request, 'getinvolved/getinvolved.html')