# Generated by Django 4.2.4 on 2023-11-15 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0014_remove_project_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='topic',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='myApp.topic'),
        ),
    ]