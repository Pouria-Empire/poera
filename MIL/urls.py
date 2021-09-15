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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from copo.views import func_login, func_question, func_scoreboard, func_main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', func_login),
    path('main', func_main),
    path('question', func_question),
    path('scoreboard', func_scoreboard),
]
urlpatterns += staticfiles_urlpatterns()
