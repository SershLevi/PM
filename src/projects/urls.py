from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    # ---Projects---
    path(
        '',
        views.ProjectListView.as_view(),
        name='projects_list'
    ),
    path(
        'create/',
        views.ProjectCreate.as_view(),
        name='project_create'
    ),
    path(
        '<slug:slug>/',
        views.ProjectDetailView.as_view(),
        name='project_detail'
    ),
    path(
        '<slug:slug>/update/',
        views.ProjectUpdate.as_view(),
        name='project_update'
    ),
    path(
        '<slug:slug>/delete/',
        views.ProjectDelete.as_view(),
        name='project_delete'
    ),
    # ---END Projects---
    # ---Tasks---
    path(
        'tasks/',
        views.TaskListView.as_view(),
        name='tasks_list'
    ),
    path(
        'tasks/create/',
        views.TaskCreate.as_view(),
        name='task_create'
    ),
    path(
        'task/<slug:slug>/',
        views.TaskDetailView.as_view(),
        name='task_detail'
    ),
    path(
        'task/<slug:slug>/update/',
        views.TaskUpdate.as_view(),
        name='task_update'
    ),
    path(
        'task/<slug:slug>/delete/',
        views.TaskDelete.as_view(),
        name='task_delete'
    ),
    # ---END Tasks---
]
