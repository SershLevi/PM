from django import forms

from .models import (
    Task,
    Project
)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'slug',
            'descriptions',
            'project_manager',
            'project_status',
            'url'
        ]



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [

        ]