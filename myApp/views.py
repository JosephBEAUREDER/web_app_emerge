from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Project, Insight, Item
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm  

def home(request):
    if request.user.is_authenticated:
        # Query the Project objects related to the logged-in user
        projects = Project.objects.filter(user=request.user)

        # Pass the projects to the template context
        context = {"projects": projects}
        return render(request, "home.html", context)
    else:
        # Handle cases where the user is not authenticated
        return render(request, "not_authenticated.html")  # Create a template for this case if needed
    
    # return render(request, 'home.html')


def create_new_project(request):
    if request.user.is_authenticated:
        Project.objects.create(user=request.user, name="New Project")
        return JsonResponse({"message": "Project created successfully"})
    else:
        return JsonResponse({"error": "User not authenticated"}, status=400)


def save_text(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            titre = data.get('titre')
            texte = data.get('texte')
            
            project = Project.objects.create(name=titre, user=request.user)
            Insight.objects.create(project=project, text=texte, swag=0)
            
            response_data = {
                "message": "Item created successfully",
            }
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"message": "Invalid request method"})


def del_project(request):
    colis = json.loads(request.body)
    id = colis["id"]

    item = Project.objects.get(id=id)
    item.delete()
    response_data = {"message": "Project deleted successfully"}
    return JsonResponse(response_data)
    

def show_all_projects(request):
    if request.user.is_authenticated:
        projects = Project.objects.filter(user=request.user)

        list_projects = []

        for project in projects:
            list_projects.append({"name": project.name, "id": project.id})
        
        reponse = {
        "projects": list_projects
    }
    return JsonResponse(reponse)


def update_project_name(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        project_id = data.get('id')
        new_name = data.get('name')

        try:
            project = Project.objects.get(id=project_id)
            project.name = new_name
            project.save()

            response_data = {'message': 'Project name updated successfully'}
            return JsonResponse(response_data)
        except Project.DoesNotExist:
            response_data = {'error': 'Project not found'}
            return JsonResponse(response_data, status=404)
        except Exception as e:
            response_data = {'error': str(e)}
            return JsonResponse(response_data, status=500)

    response_data = {'error': 'Invalid request method'}
    return JsonResponse(response_data, status=400)





# To do list

def variables(request):
    return render(request, 'variables.html')


def todolist(request):
    return render(request, 'todolist.html')

def listItems(request):
    items = Item.objects.all()
    list_items = []

    for item in items:
        list_items.append( {"titre":item.titre, "texte":item.texte, "id":item.id } )

    reponse = {
        "items": list_items
    }

    return JsonResponse(reponse)


def create_item(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            titre = data.get('titre')
            texte = data.get('texte')
            
            item = Item.objects.create(titre=titre, texte=texte)
            
            response_data = {
                "message": "Item created successfully",
                "item_id": item.id
            }
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"message": "Invalid request method"})
    

def delItem(request):
    colis = json.loads(request.body)
    identifiant = colis["identifiant"]

    item = Item.objects.get(id=identifiant)
    item.delete()

    reponse = {
        "resultat": 1
    }
    return JsonResponse(reponse)



def register(response):
    form = UserCreationForm

    return render(response, "register/register.htlm", {form})

