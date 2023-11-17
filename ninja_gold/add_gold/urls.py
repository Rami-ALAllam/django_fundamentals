

from django.urls import path
from . import views

urlpatterns = [
    path('', views.golden ),
    path('handle', views.handle),
    path('result', views.result),
    path('reset', views.reset)
]
