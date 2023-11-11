

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.num),
    path('handle', views.handle),
    path('result', views.result),
    path('end', views.end)
]