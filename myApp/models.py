from django.db import models

class Item(models.Model):
    titre = models.CharField(max_length=50) #ici on indique que ça dépassera pas 50 caractères
    texte = models.TextField()