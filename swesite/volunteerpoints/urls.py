from django.urls import path
from . import views

urlpatterns = [
    path('', views.volunteerpoints.as_view(), name='volunteerpoints'),
]