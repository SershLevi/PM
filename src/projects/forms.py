from django import forms

from .models import (
    Task,
    Project,
    Message)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'author',
            'text',
            'task',
        ]

