from django.urls import path
from events import views

urlpatterns = [
    path('past_events/', views.PastEvents.as_view(), name='pastevents'),
    path('', views.Events.as_view(), name='events'),

]
