"""
URL configuration for web_app_emerge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from myApp import views as myApp
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myApp.home),
    path('save_text/', csrf_exempt(myApp.save_text)),
    path('todolist/', myApp.todolist),
    path('todolist/list', csrf_exempt(myApp.listItems)),
    path('todolist/create_item/', csrf_exempt(myApp.create_item)),
    path('todolist/del', csrf_exempt(myApp.delItem)),
    path('accounts/', include('django.contrib.auth.urls')),
]
