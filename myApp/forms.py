from django import forms

class CreateNewProject(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    content = forms.CharField(label="Content", max_length=1000)