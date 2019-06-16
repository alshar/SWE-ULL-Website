from django.urls import path
from . import views

urlpatterns = [
    path('', views.pointtracker, name='pointtracker'),
]