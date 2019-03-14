from django import forms

from .models import (
    Task,
    Project,
    Message,
    Brand,
    Status)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
