from django.shortcuts import render
from django.http import HttpResponse


def baseindex(request):
    return render(request, 'base/baseindex.html')