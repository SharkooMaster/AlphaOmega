#!/usr/bin/env python3


from django.contrib.auth.views import LogoutView
from django.shortcuts import get_object_or_404
from django.urls import path
from django.views.generic import TemplateView

from channel.models import Channel
from channel import views as views

urlpatterns = [
    path('<str:title>',  views.main_page),

]
