from django.shortcuts import render
from django.http import HttpResponse


def getinvolved(request):
    return render(request, 'getinvolved/getinvolved.html')