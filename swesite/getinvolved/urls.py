from django.urls import path
from . import views

urlpatterns = [
    path('', views.getinvolved.as_view(), name='getinvolved'),
]