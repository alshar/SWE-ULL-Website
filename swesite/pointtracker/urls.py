from django.urls import path
from pointtracker.views import PointTrackerLoginView, PointTrackerSignUpView

urlpatterns = [
    path('signup', PointTrackerSignUpView.as_view(), name='signup'),

    path('', PointTrackerLoginView.as_view(), name='pointtracker'),
]