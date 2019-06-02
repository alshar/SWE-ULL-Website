from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('fall18/', views.fall18, name='fall18'),
]
