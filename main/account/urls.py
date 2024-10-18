#!/usr/bin/env python3


from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from account import views as views

urlpatterns = [
    path('settings/', views.settings),
    path('savesettings/', views.savesettings),
    path('signin/', views.custom_login_view),
    path('signup/', views.signup_view),
    path('addtowatchlater/<int:video>',views.addtowatchlater),
    path('removefromwatchlater/<int:video>',views.removefromwatchlater),
    path('addtowatchlater/button/<int:video>',views.addtowatchlater_button),
    path('removefromwatchlater/button/<int:video>',views.removefromwatchlater_button),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('getwatchlaterbutton/<int:video>/',views.get_watch_later_button),

]
