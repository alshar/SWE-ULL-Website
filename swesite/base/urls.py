from django.urls import path
from . import views

urlpatterns = [
    path('', views.baseindex.as_view(), name='baseindex'),
]