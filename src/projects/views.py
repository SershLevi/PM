from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)

from .forms import (
    TaskForm,
    ProjectForm, BrandForm, StatusForm, CommentForm)
from .models import (
    Project,
    Task,
    Brand, Status)


# ---Projects---

def project_list(request):
    projects_list = Project.objects.all()
    filter = ProjectForm(request.GET, queryset=Project.objects.all())
    return render(request,
                  'projects/projects_list.html',
                  {
                      'projects_list': projects_list,
                      'filter': filter,
                  })


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
# class TaskListView(ListView):
#     model = Task
#     queryset = Task.objects.all()
#
#     context_object_name = 'tasks_list'


def task_list(request):
    tasks_list = Task.objects.all()
    filter = TaskForm(request.GET, queryset=Task.objects.all())
    return render(request,
                  'projects/tasks_list.html',
                  {
                      'tasks_list': tasks_list,
                      'filter': filter,
                  })


class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'projects/forms/task_cu_form.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'projects/task_detail.html'
    context_object_name = 'task'


def task_detail(request, task_slug):
    task = get_object_or_404(
        Task,
        slug=task_slug
    )
    comments = task.comments.all()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.task = task
            new_comment.person = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request,
                  'projects/task_detail.html',
                  {
                      'task': task,
                      'comments': comments,
                      'new_comment': new_comment,
                      'comment_form': comment_form,
                  })


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'projects/forms/task_cu_form.html'


class TaskDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('tasks_list')


# ---END TASKS---


# ---Brands---
class BrandListView(ListView):
    model = Brand
    template_name = 'projects/brands_list.html'
    queryset = Brand.objects.all()

    context_object_name = 'brands_list'


class BrandCreate(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'projects/forms/brand_cu_form.html'


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'projects/brand_detail.html'
    context_object_name = 'brand'


class BrandUpdate(UpdateView):
    model = Brand
    fields = '__all__'
    template_name = 'projects/forms/brand_cu_form.html'


class BrandDelete(DeleteView):
    model = Brand
    success_url = reverse_lazy('brands_list')


# ---END Brands---
# ---Brands---
class StatusListView(ListView):
    model = Status
    template_name = 'projects/statuses_list.html'
    queryset = Status.objects.all()

    context_object_name = 'statuses_list'


class StatusCreate(CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'projects/forms/status_cu_form.html'


class StatusDetailView(DetailView):
    model = Status
    template_name = 'projects/status_detail.html'
    context_object_name = 'status'


class StatusUpdate(UpdateView):
    model = Status
    fields = '__all__'
    template_name = 'projects/forms/status_cu_form.html'


class StatusDelete(DeleteView):
    model = Status
    success_url = reverse_lazy('statuses_list')

# ---END Brands---
