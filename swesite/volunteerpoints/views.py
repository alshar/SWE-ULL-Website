from django.shortcuts import render
from django.http import HttpResponse


def volunteerpoints(request):
    return render(request, 'volunteerpoints/volunteerpoints.html')