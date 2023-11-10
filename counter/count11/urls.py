

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.count1),
    path('destroy_session', views.destroy_session),
    path('increament', views.count2),
    path('increament2', views.count3)
]
