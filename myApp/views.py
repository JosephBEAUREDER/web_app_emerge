from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Project, Insight, Item
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm  
from .forms import CreateNewProject

def home(request):
    return render(request, 'home.html')

def todolist(request):
    return render(request, 'todolist.html')




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


    # colis = json.loads(request.body)
    # text = colis['inText']

    # file_path = os.path.join(settings.MEDIA_ROOT, 'text_file.txt')
    # with open(file_path, 'a') as file:
    #     file.write(text + '\n')
    #     return JsonResponse({"message": "Text saved successfully"})
    


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


def create_project(response):
    form = CreateNewProject()
    return render(response,"home.html", {"form":form})

def create(request):
    form = CreateNewProject()
    return render(request, "create.html", {"form": form})