from django.urls import path
from pointtracker.views import PointTrackerLoginView

urlpatterns = [

    path('', PointTrackerLoginView.as_view(), name='pointtracker'),
]