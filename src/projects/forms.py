from django import forms

from projects import (
    Task,
    Project
)


# class EmailPostForm(forms.Form):
#     name = forms.CharField(max_length=25)
#     email = forms.EmailField()
#     to = forms.EmailField()
#     comments = forms.CharField(required=False,
#                                widget=forms.Textarea)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

# class SearchForm(forms.Form):
#     query = forms.CharField()
