from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    # ---Projects---
    path(
        'projects/',
        views.ProjectListView.as_view(),
        name='projects_list'
    ),
    path(
        'project/create/',
        views.ProjectCreate.as_view(),
        name='project_create',
    ),
    path(
        'project/<slug:slug>/',
        views.ProjectDetailView.as_view(),
        name='project_detail'
    ),
    path(
        'project/<slug:slug>/update/',
        views.ProjectUpdate.as_view(),
        name='project_update'
    ),
    path(
        'project/<slug:slug>/delete/',
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
        'task/create/',
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

    path(
        'message',
        views.MessageCreate.as_view(),
        name='add_message'
    ),

]
