from django.shortcuts import render
from django.http import HttpResponse


def ptindex(request):
    return render(request, 'pointstracker/ptlogin.html')
