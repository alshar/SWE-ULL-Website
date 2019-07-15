from django.urls import path
from . import views

urlpatterns = [
    path('', views.PointTrackerLogin.as_view(), name='pointtracker'),
]