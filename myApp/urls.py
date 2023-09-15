from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.home),

    path('save_text/', csrf_exempt(views.save_text)),
    path('todolist/', views.todolist),
    path('todolist/list', csrf_exempt(views.listItems)),
    path('todolist/create_item/', csrf_exempt(views.create_item)),
    path('todolist/del', csrf_exempt(views.delItem)),

    path('createproject/', views.create_project, name='create_project'),
    path("create/", views.create, name="index"),


]