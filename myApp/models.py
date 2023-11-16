from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User




class Item(models.Model):
    titre = models.CharField(max_length=50) #ici on indique que ça dépassera pas 50 caractères
    texte = models.TextField()

class Topic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="topic")
    name = models.CharField(max_length=100, default='New Topic')
    color = models.CharField(max_length=100, default="black")

    def __str__(self):
        return self.name

# create a main topic for each user when the user is created
@receiver(post_save, sender=User)
def create_main_topic(sender, instance, created, **kwargs):
    if created:
        Topic.objects.create(user=instance, name="Main", color="black")


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project", null=True)
    name = models.CharField(max_length=100)
    text = models.TextField(default="Write about this project")
    goals = models.TextField(default="Write about the goals of this project")
    approach = models.TextField(default=" ")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="projects", null=True, default=None)    

    def save(self, *args, **kwargs):
        if self.topic is None:
            main_topic = Topic.objects.filter(name="Main").first()
            if main_topic is not None:
                self.topic = main_topic
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Insight(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    swag = models.IntegerField(default=0)

    def __str__(self):
        return self.text
    
