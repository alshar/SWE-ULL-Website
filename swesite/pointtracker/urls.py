from django.urls import path
from pointtracker.views import PointTrackerView

urlpatterns = [
    path('', PointTrackerView.as_view(), name='pointtracker'),
]