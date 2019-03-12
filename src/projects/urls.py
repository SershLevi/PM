from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path(
        '',
        views.ProjectListView.as_view(),
        name='projects_list'
    ),
    path(
        'project/create/',
        views.ProjectCreate.as_view(),
        name='project_create'
    ),

    path(
        'project/<slug:slug>/',
        views.ProjectDetailView.as_view(),
        name='project_detail'
    ),

    path(
        'project/<slug:slug>/update',
        views.ProjectUpdate.as_view(),
        name='project_update'
    ),
    path(
        'project/<slug:slug>/delete',
        views.ProjectDelete.as_view(),
        name='project_delete'
    ),

    path(
        'tasks/',
        views.TaskListView.as_view(),
        name='tasks_list'
    ),

    path(
        'task/<slug:slug>/',
        views.TaskDetailView.as_view(),
        name='task_detail'
    ),
]
