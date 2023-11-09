from django.urls import path
from . import views

urlpatterns = [
    path('time1', views.time1),
    path('time2', views.time2),
    path('time3', views.time3)
]