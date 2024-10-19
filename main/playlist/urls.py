#!/usr/bin/env python3


from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from playlist import views as views

urlpatterns = [
    path('<str:name>', views.playlist),
    path('createnewplaylist/', views.create_new_playlist),
    path('settitle/<int:pk>/', views.set_title),
    path('getplaylistpopup/<int:video>/', views.get_playlist_popup),
    path('addvideo/<int:playlist>/<int:video>/',views.addvideo),
    path('removevideo/<int:playlist>/<int:video>/',views.removevideo),
    path('getlink/<int:pk>/',views.get_link),

]
