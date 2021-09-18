"""MIL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from copo.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', func_main, name='main'),
    path('accounts/login/', func_login),
    path('accounts/register/', func_register),
    path('accounts/logout/', func_logout),
    path('question', func_question),
    path('scoreboard', func_scoreboard),
    path('back', func_goBack),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
