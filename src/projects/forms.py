import django_filters
from django import forms

from .models import *


class ProjectForm(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = '__all__'

class TaskForm(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = '__all__'

    creation_year = django_filters.NumberFilter(field_name='creation_timestamp', lookup_expr='year')
    creation_month = django_filters.NumberFilter(field_name='creation_timestamp', lookup_expr='month')


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['person', 'task']
