from django.urls import path
from pointtracker.views import PointTrackerLogin

urlpatterns = [
    path('', PointTrackerLogin.as_view(), name='pointtracker'),
]