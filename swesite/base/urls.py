from django.urls import path
from . import views

urlpatterns = [
    path('', views.baseindex, name='baseindex'),
]