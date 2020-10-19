from django.urls import path
from . import views
from weather.urls import *
from note.urls import *

urlpatterns = [
    path('', views.index),
]