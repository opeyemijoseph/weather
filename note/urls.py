from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_index, name='note_index'),
    path('create', views.create_note),
    path('delete/<id>/', views.delete_note, name='delete_note')
]