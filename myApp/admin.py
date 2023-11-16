from django.contrib import admin
from .models import Item, Project, Insight, Topic

# Register your models here.
admin.site.register(Item)
admin.site.register(Project)
admin.site.register(Insight)
admin.site.register(Topic)