from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.home),

    path('save_text/', csrf_exempt(views.save_text)),
    path('create_new_project/', csrf_exempt(views.create_new_project), name='create_new_project'),
    path("del_project/", csrf_exempt(views.del_project), name="del_project"),
    path("show_all_projects", csrf_exempt(views.show_all_projects), name="show_all_projects"),
    path("update_project_name", csrf_exempt(views.update_project_name), name= "update_project_name"),

    path('todolist/', views.todolist),
    path('todolist/list', csrf_exempt(views.listItems)),
    path('todolist/create_item/', csrf_exempt(views.create_item)),
    path('todolist/del', csrf_exempt(views.delItem)),

    path("variables/", views.variables),

]