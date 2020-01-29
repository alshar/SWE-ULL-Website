from django.urls import path
from events import views

urlpatterns = [
    path('fall18/', views.fall18.as_view(), name='fall18'),
    path('spring18/', views.spring18.as_view(), name='spring18'),
    path('spring19/', views.spring19.as_view(), name='spring19'),
    path('fall19/', views.fall19.as_view(), name='fall19'),

    path('', views.events.as_view(), name='events'),

]
