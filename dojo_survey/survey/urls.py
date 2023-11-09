

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.survey),
    path('result', views.result),
]