from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('note/<uniqid>', views.note, name='note'),
    path('add_note', views.add_note, name='add_note')
]