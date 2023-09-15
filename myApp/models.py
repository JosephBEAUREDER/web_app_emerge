from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    titre = models.CharField(max_length=50) #ici on indique que ça dépassera pas 50 caractères
    texte = models.TextField()


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project", null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Insight(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    swag = models.IntegerField(default=0)

    def __str__(self):
        return self.name