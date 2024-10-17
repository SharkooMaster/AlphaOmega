#!/usr/bin/env python3


from django.urls import path

from account import views as views

urlpatterns = [
    path('signin/', views.custom_login_view),
    path('signup/', views.signup_view),
    path('playlists/', views.playlists),
]
