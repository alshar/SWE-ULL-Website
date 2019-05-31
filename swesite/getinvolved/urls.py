from django.urls import path
from . import views

urlpatterns = [
    path('', views.getinvolved, name='getinvolved'),
]