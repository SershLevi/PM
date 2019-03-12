from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)

from .forms import (
    ProjectForm,
    TaskForm,
)
from .models import (
    Project,
    Task,
)


# ---Projects---
class ProjectListView(ListView):
    model = Project
    template_name = 'projects/projects_list.html'
    queryset = Project.objects.all()

    context_object_name = 'projects_list'


class ProjectCreate(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/forms/project_cu_form.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'


class ProjectUpdate(UpdateView):
    model = Project
    fields = '__all__'
    template_name = 'projects/forms/project_cu_form.html'


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('projects_list')


# ---END PROJECTS---

# ---Tasks---
class TaskDetailView(DetailView):
    model = Task
    template_name = 'projects/task_detail.html'
    context_object_name = 'task'


class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'projects/forms/task_cu_form.html'


class TaskListView(ListView):
    model = Task
    template_name = 'projects/tasks_list.html'
    queryset = Task.objects.all()

    context_object_name = 'tasks_list'


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'projects/forms/task_cu_form.html'


class TaskDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('tasks_list')

# ---END TASKS---
