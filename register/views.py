from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from myApp.models import Project

# Create your views here.
def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            user = form.save()

            Project.objects.create(user=user, name="Create new Project")

            # # Log in the user
            # login(request, user)

            return redirect("/")
    else:
        form = UserCreationForm()
        
    return render(response, "register/register.html", {"form":form})