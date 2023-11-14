from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.home),
    path("show_all_projects", csrf_exempt(views.show_all_projects), name="show_all_projects"),
    path('edit_project/<int:project_id>/', views.edit_project, name='edit_project'),
    path('edit_project/<int:project_id>/update_project_text/', csrf_exempt(views.update_project_text), name='update_project_text'),
    path("create_project/", csrf_exempt(views.create_project), name="create_project"),
]