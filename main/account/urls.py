#!/usr/bin/env python3


from django.contrib.auth.views import LogoutView
from django.urls import path

from account import views as views

urlpatterns = [
    path('settings/', views.settings),
    path('savesettings/', views.savesettings),
    path('signin/', views.custom_login_view),
    path('signup/', views.signup_view),
    path('playlist/<str:name>', views.playlist),
    path('addtowatchlater/<int:video>',views.addtowatchlater),
    path('removefromwatchlater/<int:video>',views.removefromwatchlater),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('playlist/createnewplaylist/', views.create_new_playlist),
    path('playlist/settitle/<int:pk>/', views.set_title),

]
