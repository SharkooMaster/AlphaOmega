"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

from page import views as page_views

urlpatterns = [
    path('admin/', admin.site.urls),
	path("", page_views.index, name="index"),
	path("page/video/", page_views.addor_and_show, name="index"),
	path("page/video", page_views.addor_and_show, name="index"),
	path("account/", include("account.urls")),
	path("channel/", include("channel.urls")),
	path("playlist/", include("playlist.urls")),
	path("video/<str:video_id>/", page_views.showVideo, name="video"),
	path("search", page_views.search, name="search")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
