from django.urls import path
from events import views

urlpatterns = [
    path('', views.events.as_view(), name='events'),
    path('fall18/', views.fall18.as_view(), name='fall18'),
    path('spring18', views.spring18.as_view(), name='spring18')
]
