from django.urls import path
from . import views

urlpatterns = [
    path('', views.ptindex, name='ptindex'),
]