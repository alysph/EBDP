from django.urls import path

from EBDPApp import views
from . import views



urlpatterns = [
    path('', views.cont, name="Cont"),
]
