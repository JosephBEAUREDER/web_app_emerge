from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from myApp.models import Project, Insight, Item, Topic
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json


def home(request):    
    return render(request, 'test_1/home_test_1.html')

def show_all_topics(request):
    if request.method == 'POST' and request.user.is_authenticated:

        # get all the projects of the user
        projects = Project.objects.filter(user=request.user)
        list_projects = []
        for project in projects:
            list_projects.append({"name": project.name, "id": project.id})


        # get all the topics of the user
        topics = list(Topic.objects.filter(user=request.user))
        # topics = Topic.objects.filter(user=request.user)
        list_topics = []
        for topic in topics:
            list_topics.append({"name": topic.name, "id": topic.id, "color": topic.color})
        

        reponse = {
        "projects": list_projects,
        "topics": list_topics,
    }
        
    return JsonResponse(reponse)




def show_all_project(request):
    if request.user.is_authenticated:

        # get all the projects of the user
        projects = Project.objects.filter(user=request.user)
        list_projects = []
        for project in projects:
            list_projects.append({"name": project.name, "id": project.id, "color": project.topic.color})

        # get all the topics of the user
        topics = list(Topic.objects.filter(user=request.user))
        list_topics = []
        for topic in topics:
            list_topics.append({"name": topic.name, "id": topic.id, "color": topic.color})
        

        reponse = {
        "projects": list_projects,
        "topics": list_topics,
    }
    return JsonResponse(reponse)




def edit_project(request, project_id):
    
   # get the name of the project
    project = Project.objects.get(id=project_id)

    return render(request, 'test_1/edit_project.html', {'project': project})





def create_project(request):
    if request.user.is_authenticated:
        Project.objects.create(user=request.user, name="New Project")
        return JsonResponse({"message": "Project created successfully"})
    else:
        return JsonResponse({"error": "User not authenticated"}, status=400)
   




@csrf_exempt
def update_project_text(request, project_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        project_id = data.get('project_id')
        new_text = data.get('new_text')

        try:
            # Get the project and update the text
            project = Project.objects.get(id=project_id)
            project.text = new_text
            project.save()

            # Return a JSON response
            return JsonResponse({'status': 'success'})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Project not found'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})





